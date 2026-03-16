FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock* ./

RUN poetry install --no-root --no-interaction 

COPY . .

RUN mkdir -p /app/tmp/uploads

EXPOSE 8000

