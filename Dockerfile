FROM python:3.10-slim-buster

# Set working directory
WORKDIR /app

# Install dependencies first (better cache usage)
COPY requirements.txt /app/

# Install dependencies without cache (smaller image)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . /app/

# Default command
CMD ["python3", "app.py"]
