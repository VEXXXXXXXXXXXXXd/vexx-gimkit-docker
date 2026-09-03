FROM python:3.10-slim

# Install system dependencies for Chromium + Playwright
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    ca-certificates \
    libx11-6 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libpangocairo-1.0-0 \
    libnss3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxkbcommon0 \
    libxshmfence1 \
    libglu1-mesa \
    libxfixes3 \
    libpango-1.0-0 \
    libxext6 \
    libxrender1 \
    libxi6 \
    libxtst6 \
    libgtk-3-0 \
    libgdk-pixbuf2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Install Playwright + Chromium
RUN pip install playwright
RUN playwright install chromium

# Copy project files
WORKDIR /app
COPY . .

# Install Python dependencies
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
