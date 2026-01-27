# Dockerfile for Order Management System

FROM python:3.12-slim-bookworm

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Create non-root user that matches the host user in the docker-compose (UID 1000)
RUN groupadd -g 1000 zenith && \
    useradd -u 1000 -g 1000 -m zenith && \
    mkdir -p /app/logs && \
    chown -R zenith:zenith /app

# Switch to non-root user early to ensure installed files are owned by zenith if needed
# But for pip system install we still need root, so we do it first.
COPY README.md pyproject.toml .env* ./
RUN uv pip install --system .

# Copy source code and ensure ownership
COPY --chown=zenith:zenith . .

# Set user
USER zenith

# Expose port
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
