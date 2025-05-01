FROM python:3.11-slim

# Install required packages
RUN apt-get update && apt-get install -y bash gcc libffi-dev libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy app
WORKDIR /app
COPY . /app

# Install Python dependencies
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "app.py"]

