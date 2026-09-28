# Use an official Locust image as the base
FROM locustio/locust

USER root

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    jq \
    vim \
    procps \
    less \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install zstandard to support zstd Accept-Encoding with HttpUser
RUN pip install --no-cache-dir zstandard

WORKDIR /app

# Create application directories
RUN mkdir -p /app/common /app/locustfiles /app/data /app/reports

# Copy application files
COPY common /app/common
COPY locustfiles /app/locustfiles
COPY data /app/data
COPY start_worker.sh /start_worker.sh

# Configure permissions
RUN chmod 777 /app/reports && chmod +x /start_worker.sh

EXPOSE 8089

ENTRYPOINT locust --master -f $TEST_FILE --loglevel WARNING
