FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

"""
# Use the official Python image as a base
# Use Python 3.12 slim for a secure, lightweight 2025 base
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies first to use Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose the port Gunicorn will listen on
EXPOSE 5000

# Run with Gunicorn for production-grade performance
# 'app:app' assumes your main file is app.py and the Flask variable is 'app'
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
"""