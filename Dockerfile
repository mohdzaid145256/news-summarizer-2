# Use Python 3.10 (stable with newspaper3k)
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirement file first (for better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the app
COPY . .

# Expose port for Flask
EXPOSE 5000

# Start with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
