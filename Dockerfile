FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PORT=8000
WORKDIR /srv
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Refresh the knowledge base at build time; falls back to bundled seed data if the sites block the build host.
ARG SCRAPE=1
RUN if [ "$SCRAPE" = "1" ]; then timeout 600 python scrape.py --max-wasalt 40 --max-darglobal 38 || python scrape.py --seed-only; else python scrape.py --seed-only; fi
RUN useradd -m bot && chown -R bot /srv
USER bot
EXPOSE 8000
CMD gunicorn -w 1 --threads 4 -b 0.0.0.0:${PORT} --timeout 200 main:app
