FROM python:3.10-slim

# Set workdir
WORKDIR /app

# Install system deps for Postgres client
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# Copy and install Python deps
COPY requirements.txt .
ENV PIP_DEFAULT_TIMEOUT=100
RUN pip install --no-cache-dir -r requirements.txt
# Copy project
COPY . .

# Default command
CMD ["bash"]
