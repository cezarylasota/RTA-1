FROM python:3.10-slim

# katalog roboczy
WORKDIR /app

COPY app.py .

RUN pip install flask

# Uruchomomienie aplikacji
CMD ["python", "app.py"]
