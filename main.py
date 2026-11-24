"""Real-estate chatbot: retrieval over scraped DarGlobal + Wasalt data, answers by an OpenRouter free model."""
from __future__ import annotations

import json
import logging
import os
import re
from pathlib import Path

import requests
from flask import Flask, jsonify, request, send_from_directory
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

ROOT = Path(__file__).resolve().parent
DATA = Path(os.getenv("KNOWLEDGE_FILE", ROOT / "knowledge.json"))
OPENROUTER_URL = os.getenv("OPENROUTER_URL", "https://openrouter.ai/api/v1/chat/completions")
API_KEY = os.getenv("OPENROUTER_API_KEY", "")
# openrouter/free picks an available free model at random, so retrying it gives a different model each time.
MODELS = [m.strip() for m in os.getenv("OPENROUTER_MODELS", "openrouter/free").split(",") if m.strip()]
ATTEMPTS = int(os.getenv("LLM_ATTEMPTS", "4"))
TOP_K = int(os.getenv("TOP_K", "8"))

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("bot")
app = Flask(__name__, static_folder=str(ROOT), static_url_path="/static")

FIELDS = ["source", "type", "purpose", "title", "brand", "city", "district", "country", "status",
          "property_types", "price", "bedrooms", "bathrooms", "area", "size", "text"]


def as_doc(r: dict) -> str:
    return " | ".join(f"{k}: {r[k]}" for k in FIELDS if r.get(k) not in (None, ""))


RECORDS: list[dict] = json.loads(DATA.read_text(encoding="utf-8"))
DOCS = [as_doc(r) for r in RECORDS]
VEC = TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True, stop_words="english")
MATRIX = VEC.fit_transform(DOCS)
log.info("Loaded %d records from %s", len(RECORDS), DATA)


def retrieve(query: str, k: int = TOP_K) -> list[dict]:
    q = query.lower()
    scores = linear_kernel(VEC.transform([query]), MATRIX).ravel()
    beds = re.search(r"(\d+)\s*-?\s*(?:bed|br\b|bhk|bedroom)", q)
    want_apt, want_villa = bool(re.search(r"apartment|flat|studio", q)), "villa" in q
    for i, r in enumerate(RECORDS):  # light boosts for explicit intent
        title = r["title"].lower()
        if beds and str(r.get("bedrooms", "")) == beds.group(1):
            scores[i] += 0.15
        if want_apt and "apartment" in title:
            scores[i] += 0.08
        if want_villa and "villa" in title:
            scores[i] += 0.08
        if re.search(r"\bwhat is\b|\bwho (is|are)\b|about (the )?company", q) and r["type"] == "company":
            scores[i] += 0.2
        if "wasalt" in q and r["source"] == "Wasalt":
            scores[i] += 0.15
        if ("darglobal" in q or "dar global" in q) and r["source"] == "DarGlobal":
            scores[i] += 0.15
        if r.get("purpose") and re.search(r"\b(rent|lease)\b", q) and r["purpose"] == "rent":
            scores[i] += 0.1
        if r.get("purpose") and re.search(r"\b(buy|sale|purchase)\b", q) and r["purpose"] == "sale":
            scores[i] += 0.1
        city = (r.get("city") or "").lower()
        if city and any(part and part in q for part in re.split(r"[,()]\s*", city)):
            scores[i] += 0.12
        country = (r.get("country") or "").lower()
        if country and (country != "saudi arabia" or r["type"] == "project") and country in q:
            scores[i] += 0.12
    idx = scores.argsort()[::-1][:k]
    return [RECORDS[i] | {"score": round(float(scores[i]), 3)} for i in idx if scores[i] > 0]


SYSTEM = (
    "You are a helpful real-estate assistant for properties from DarGlobal (luxury branded developments in the UAE, "
    "Saudi Arabia, Oman, Qatar, Spain and the UK) and Wasalt (Saudi Arabia's property listing platform). "
    "Answer ONLY from the CONTEXT records. If the answer is not there, say you don't have that information and suggest "
    "the relevant website. Quote prices exactly as given with currency. Keep answers concise; use short bullet lists "
    "for multiple properties. End with the source URL(s) you used as markdown links. Do not give financial advice."
)


def call_openrouter(messages: list[dict]) -> tuple[str, str]:
    if not API_KEY:
        raise RuntimeError("OPENROUTER_API_KEY not set")
    last = None
    for model in [m for m in MODELS for _ in range(ATTEMPTS)]:
        try:
            r = requests.post(OPENROUTER_URL, timeout=45, headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
                "HTTP-Referer": os.getenv("APP_URL", "http://localhost:8000"),
                "X-Title": "DarGlobal & Wasalt Property Chatbot",
            }, json={"model": model, "messages": messages, "temperature": 0.2, "max_tokens": 2000})
            if r.status_code != 200:
                last = f"{model}: HTTP {r.status_code} {r.text[:200]}"
                log.warning(last)
                continue
            body = r.json()
            text = body["choices"][0]["message"]["content"]
            if text and text.strip():
                return text.strip(), body.get("model", model)
            last = f"{body.get('model', model)}: empty answer"
            log.warning(last)
        except (requests.RequestException, KeyError, ValueError) as e:
            last = f"{model}: {e}"
            log.warning(last)
    raise RuntimeError(last or "no model answered")


def fallback_answer(hits: list[dict]) -> str:
    if not hits:
        return "I couldn't find anything matching that in the DarGlobal or Wasalt data."
    lines = ["Here's what I found in the collected data (LLM unavailable, showing raw matches):"]
    for h in hits[:4]:
        bits = [h.get("city"), h.get("price"), h.get("status")]
        lines.append(f"- **{h['title']}** ({h['source']}) – " + ", ".join(b for b in bits if b) + f" [link]({h['url']})")
    return "\n".join(lines)


@app.get("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


@app.get("/api/health")
def health():
    return jsonify(ok=True, records=len(RECORDS), llm_configured=bool(API_KEY), models=MODELS)


@app.get("/api/search")
def search():
    return jsonify(retrieve(request.args.get("q", ""), int(request.args.get("k", TOP_K))))


@app.post("/api/chat")
def chat():
    body = request.get_json(silent=True) or {}
    history = [m for m in body.get("messages", []) if m.get("role") in ("user", "assistant")][-8:]
    if not history or history[-1]["role"] != "user":
        return jsonify(error="last message must be from the user"), 400
    question = history[-1]["content"][:2000]
    # include previous user turn so follow-ups ("what about rent there?") retrieve well
    prev_user = next((m["content"] for m in reversed(history[:-1]) if m["role"] == "user"), "")
    hits = retrieve(f"{question} {prev_user}"[:2500])
    context = "\n\n".join(f"[{i+1}] {as_doc(h)} | url: {h['url']}" for i, h in enumerate(hits))
    messages = [{"role": "system", "content": SYSTEM}] + history[:-1] + [
        {"role": "user", "content": f"CONTEXT:\n{context or '(no matching records)'}\n\nQUESTION: {question}"}]
    try:
        answer, model = call_openrouter(messages)
    except RuntimeError as e:
        log.warning("LLM fallback: %s", e)
        answer, model = fallback_answer(hits), None
    return jsonify(answer=answer, model=model,
                   sources=[{"title": h["title"], "url": h["url"], "source": h["source"]} for h in hits[:4]])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8000")))
