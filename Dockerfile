FROM python:3.10-slim

# Safe defaults
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY . .

# Expose Flask/Gunicorn port
EXPOSE 5000

# Start with Gunicorn (app module: 'app', object: 'app')
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
