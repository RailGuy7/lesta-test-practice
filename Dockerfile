# Use lightweight python 3.9 image to save disk space
FROM python:3.9-slim

# Install dependencies
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy application into container
COPY app.py .

# Start the application
CMD ["python3", "app.py"]
