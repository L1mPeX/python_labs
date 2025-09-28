FROM python:3.11-slim

WORKDIR /app

COPY lab02/ lab02/
COPY requirements.txt .

RUN pip install --no-cache-dir -r lab02/requirements.txt

CMD ["pytest", "-v", "lab02/tests"]
