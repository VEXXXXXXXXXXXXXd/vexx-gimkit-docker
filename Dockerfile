FROM mcr.microsoft.com/playwright/python:v1.48.0-focal

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "app.py"]
