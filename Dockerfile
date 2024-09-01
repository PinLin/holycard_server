FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get install -y build-essential curl libpq-dev

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

COPY pyproject.toml poetry.lock* /app/

RUN poetry install --no-root

COPY . /app/

RUN poetry run python manage.py collectstatic --noinput

ENTRYPOINT ["/app/entrypoint.sh"]

EXPOSE 8000
