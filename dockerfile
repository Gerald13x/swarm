# Use official Python image as base
FROM python:3.9-slim

# Define volume for persistent storage 
VOLUME /app/data

# Create data directory for SQLite 
RUN mkdir -p /app/data 

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port 5000
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]