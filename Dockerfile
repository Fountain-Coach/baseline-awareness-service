FROM python:3.11-slim AS base

WORKDIR /app

# Install runtime dependencies only
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt uvicorn

# Copy everything (including app folder)
COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.entrypoint:app", "--host", "0.0.0.0", "--port", "8000"]