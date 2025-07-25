# ---- Dockerfile ----
# Use official Python 3.13 slim image
FROM python:3.13-slim

# Create work directory inside the container
WORKDIR /app

# Copy requirements first and install -- faster rebuilds
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project into the image
COPY . .

# Default command → run the CLI
ENTRYPOINT ["python", "cli.py"]
