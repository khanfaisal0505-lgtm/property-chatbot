# Property Assistant: DarGlobal + Wasalt chatbot

A retrieval-augmented chatbot over public data from **darglobal.co.uk** (luxury branded developments) and **wasalt.sa** (Saudi listings). It answers with a **free OpenRouter model** (`openrouter/free` by default, with fallbacks to other `:free` models).

```
scrape.py        polite scraper (robots.txt, 1.5 s delay) -> knowledge.json
seed_records.py  66 records collected Nov 2026 (fallback if scraping is blocked)
main.py          Flask API: TF-IDF retrieval + OpenRouter call, retrieval-only fallback
index.html       chat UI
Dockerfile, docker-compose.yml, render.yaml
```

## Run locally

```bash
cp .env.example .env          # add your key from https://openrouter.ai/keys (free)
docker compose up --build     # open http://localhost:8000
```

`docker build --build-arg SCRAPE=0 .` skips the live scrape and uses the bundled data.

## Deploy (gives a public URL)

**Render (free tier):** push this folder to a GitHub repo, then go to Render, click New, and choose Blueprint. Render reads `render.yaml` and builds the Dockerfile. Set `OPENROUTER_API_KEY`, and you get `https://property-chatbot.onrender.com`.

**Hugging Face Spaces:** create a Docker Space, push these files, and add `OPENROUTER_API_KEY` as a secret. Set `PORT=7860` in the Space variables.

## API

- `POST /api/chat` with body `{"messages":[{"role":"user","content":"..."}]}`. It returns `{answer, model, sources}`.
- `GET /api/search?q=...&k=6` returns the retrieval hits.
- `GET /api/health`

## Notes

- Only public pages are fetched, and robots.txt is respected. Prices and availability change, so the bot cites source URLs.
- If no key is set or every free model is rate-limited, the bot still replies, with the top matching records.
- OpenRouter free tier limits: about 20 requests/min and 50 requests/day without credits.
