FROM python:3.9-slim

WORKDIR /app

# biar python ga buffering & ga bikin file .pyc
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "uts.py"]