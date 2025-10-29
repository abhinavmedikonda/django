##########################
# Stage 1: Build on Ubuntu
##########################
FROM ubuntu:22.04 AS build

WORKDIR /app

# Install Python + build tools
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Build wheels for all dependencies
RUN pip3 wheel --no-cache-dir --wheel-dir /wheels -r requirements.txt


##########################
# Stage 2: Runtime (Python slim)
##########################
FROM python:3.11-slim-bookworm

WORKDIR /app

# Install runtime system dependencies (if your DB needs them)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY --from=build /wheels /wheels
RUN pip install --no-cache-dir /wheels/*

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
