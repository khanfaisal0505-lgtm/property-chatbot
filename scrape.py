"""Scrape public pages from DarGlobal and Wasalt into knowledge.json.

Polite: honours robots.txt, 1.5 s delay between requests, small page caps.
If a site is unreachable the bundled seed records (collected Nov 2026) are kept,
so the chatbot always has a knowledge base.

Usage:  python scrape.py [--max-wasalt 60] [--max-darglobal 40] [--out knowledge.json]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path
from urllib import robotparser
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

sys.path.insert(0, str(Path(__file__).parent))
from seed_records import SEED  # noqa: E402

UA = "Mozilla/5.0 (compatible; RealEstateChatbotResearch/1.0)"
DELAY = 1.5
session = requests.Session()
session.headers.update({"User-Agent": UA, "Accept-Language": "en"})
_robots: dict[str, robotparser.RobotFileParser] = {}


def allowed(url: str) -> bool:
    host = f"{urlparse(url).scheme}://{urlparse(url).netloc}"
    if host not in _robots:
        rp = robotparser.RobotFileParser()
        try:
            r = session.get(host + "/robots.txt", timeout=15)
            rp.parse(r.text.splitlines() if r.ok else [])
        except requests.RequestException:
            rp.parse([])
        _robots[host] = rp
    return _robots[host].can_fetch(UA, url)


def get(url: str) -> BeautifulSoup | None:
    if not allowed(url):
        print(f"  robots.txt disallows {url}")
        return None
    try:
        time.sleep(DELAY)
        r = session.get(url, timeout=25)
        r.raise_for_status()
        return BeautifulSoup(r.text, "html.parser")
    except requests.RequestException as e:
        print(f"  ! {url}: {e}")
        return None


def clean(text: str, limit: int = 1800) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return text[:limit]


def page_text(soup: BeautifulSoup) -> str:
    for t in soup(["script", "style", "noscript", "svg", "header", "footer", "nav"]):
        t.decompose()
    main = soup.find("main") or soup.body or soup
    return clean(main.get_text(" "))


def meta(soup: BeautifulSoup, name: str) -> str:
    tag = soup.find("meta", attrs={"name": name}) or soup.find("meta", attrs={"property": name})
    return (tag.get("content") or "").strip() if tag else ""


# ---------------------------------------------------------------- DarGlobal
def scrape_darglobal(limit: int) -> list[dict]:
    base = "https://darglobal.co.uk"
    print("DarGlobal: projects index")
    soup = get(f"{base}/projects")
    if not soup:
        return []
    links = []
    for a in soup.find_all("a", href=True):
        href = urljoin(base, a["href"].split("#")[0])
        if urlparse(href).netloc.endswith("darglobal.co.uk") and href.rstrip("/") != f"{base}/projects":
            path = urlparse(href).path.strip("/")
            if path and not path.startswith(("news", "media", "careers", "contact", "investor", "partners", "product-category")):
                links.append(href)
    links = list(dict.fromkeys(links))[:limit]
    out = []
    for url in links:
        print("  ", url)
        s = get(url)
        if not s:
            continue
        title = (s.find("h1").get_text(" ", strip=True) if s.find("h1") else "") or (s.title.string if s.title else url)
        desc = meta(s, "description")
        out.append(dict(source="DarGlobal", type="project", title=clean(title, 140), url=url,
                        text=clean(f"{desc} {page_text(s)}")))
    return out


# ------------------------------------------------------------------- Wasalt
WASALT_INDEXES = [
    "https://wasalt.sa/en/properties-for-sale-in-riyadh",
    "https://wasalt.sa/en/properties-for-sale-in-jeddah",
    "https://wasalt.sa/en/properties-for-rent-in-riyadh",
    "https://wasalt.sa/en/properties-for-rent-in-jeddah",
    "https://wasalt.sa/en/apartments-for-sale-in-khobar",
    "https://wasalt.sa/en/properties-for-sale-in-dammam",
]


def _from_next_data(soup: BeautifulSoup) -> dict:
    """Wasalt is a Next.js site; listing details often sit in __NEXT_DATA__."""
    tag = soup.find("script", id="__NEXT_DATA__")
    if not tag or not tag.string:
        return {}
    try:
        data = json.loads(tag.string)
    except json.JSONDecodeError:
        return {}
    found: dict = {}

    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                kl = k.lower()
                if kl in ("price", "salePrice", "rentprice") and isinstance(v, (int, float, str)) and "price" not in found:
                    found["price"] = v
                elif kl in ("bedrooms", "noofbedrooms", "bedroomcount") and "bedrooms" not in found:
                    found["bedrooms"] = v
                elif kl in ("city", "cityname") and isinstance(v, str) and "city" not in found:
                    found["city"] = v
                walk(v)
        elif isinstance(o, list):
            for i in o[:50]:
                walk(i)

    walk(data.get("props", {}))
    return found


def scrape_wasalt(limit: int) -> list[dict]:
    links = []
    for idx in WASALT_INDEXES:
        print("Wasalt index:", idx)
        s = get(idx)
        if not s:
            continue
        for a in s.find_all("a", href=True):
            href = urljoin("https://wasalt.sa", a["href"])
            if "/property/" in href:
                links.append(href.split("?")[0])
    links = list(dict.fromkeys(links))[:limit]
    out = []
    for url in links:
        print("  ", url)
        s = get(url)
        if not s:
            continue
        extra = _from_next_data(s)
        title = s.find("h1").get_text(" ", strip=True) if s.find("h1") else (s.title.string if s.title else "Listing")
        purpose = "rent" if "/rent/" in url else "sale"
        rec = dict(source="Wasalt", type="listing", purpose=purpose, title=clean(title, 140), url=url,
                   country="Saudi Arabia", text=clean(page_text(s)))
        for k in ("price", "bedrooms", "city"):
            if k in extra:
                rec[k] = extra[k]
        out.append(rec)
    return out


def merge(seed: list[dict], scraped: list[dict]) -> list[dict]:
    by_url = {r["url"] + "|" + r["title"]: r for r in seed}
    for r in scraped:
        same = [k for k in by_url if k.startswith(r["url"] + "|")]
        if same:  # refresh the seed record's text with live content, keep curated fields
            by_url[same[0]]["text"] = (by_url[same[0]]["text"] + " " + r["text"])[:2500]
        else:
            by_url[r["url"] + "|" + r["title"]] = r
    recs = list(by_url.values())
    for i, r in enumerate(recs):
        r["id"] = i
    return recs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-wasalt", type=int, default=60)
    ap.add_argument("--max-darglobal", type=int, default=40)
    ap.add_argument("--out", default=str(Path(__file__).parent / "knowledge.json"))
    ap.add_argument("--seed-only", action="store_true", help="write the bundled records without scraping")
    a = ap.parse_args()
    scraped = [] if a.seed_only else scrape_darglobal(a.max_darglobal) + scrape_wasalt(a.max_wasalt)
    recs = merge([dict(r) for r in SEED], scraped)
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(recs, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Wrote {len(recs)} records ({len(scraped)} scraped live) -> {a.out}")


if __name__ == "__main__":
    main()
