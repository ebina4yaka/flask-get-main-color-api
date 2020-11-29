FROM python:3.9.0-slim as builder

WORKDIR /usr/src/app

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry export -f requirements.txt > requirements.txt


FROM python:3.9.0-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY --from=builder /usr/src/app/requirements.txt .

RUN pip install gunicorn
RUN pip install -r requirements.txt

RUN apt-get update
RUN apt-get install -y libgl1-mesa-dev libopencv-dev

COPY . .

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app
