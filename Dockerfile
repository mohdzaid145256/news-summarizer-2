# Use official Python image
FROM python:3.12-slim

# Prevent Python from buffering logs
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy dependency list and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Expose port 5000 for Flask
EXPOSE 5000

# Command to run the app with Gunicorn (for production)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
