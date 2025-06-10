# Use a lightweight official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install any system dependencies you might need
RUN apt-get update && apt-get install -y build-essential

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your entire project into the container
COPY . .

# Ensure the PORT variable defaults to 8080 (used by Fly.io)
ENV PORT=8080

# Run Gunicorn on your Flask app (main.py defines app = Flask(__name__))
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "main:app", "--workers=4"]
