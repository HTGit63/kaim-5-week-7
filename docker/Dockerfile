FROM python:3.10

# Set workdir
WORKDIR /app

# Install system deps for Postgres client
RUN apt-get update && apt-get install -y --no-install-recommends libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# Copy and install Python deps
COPY requirements.txt .
ENV PIP_DEFAULT_TIMEOUT=500
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Copy configuration files
COPY files/profiles.yml /root/.dbt/profiles.yml
COPY files/dbt_project.yml /app/dbt_project.yml

# Default command
CMD ["tail", "-f", "/dev/null"]
