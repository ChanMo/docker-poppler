FROM python:3-slim
MAINTAINER Chan Mo <chan.mo@outlook.com>

RUN apt-get update && \
    apt-get install -y poppler-utils && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN python3 -m pip install flask gunicorn
COPY app.py .
RUN mkdir media

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", ":5000", "app:app"]
