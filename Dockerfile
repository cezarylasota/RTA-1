# Użyj oficjalnego obrazu Pythona
FROM python:3.10-slim

# Ustaw katalog roboczy
WORKDIR /app

# Skopiuj plik aplikacji do kontenera
COPY app.py .

# Zainstaluj Flask
RUN pip install flask

# Uruchom aplikację
CMD ["python", "app.py"]
