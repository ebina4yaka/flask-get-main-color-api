FROM python:3.9.0-slim as builder

WORKDIR /usr/src/app

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry export -f requirements.txt > requirements.txt


FROM python:3.8-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY --from=builder /usr/src/app/requirements.txt .

RUN pip install -r requirements.txt

RUN apt-get update
RUN apt-get install -y libgl1-mesa-dev libopencv-dev

COPY . .

CMD flask run --host=0.0.0.0 --port=$PORT
