FROM python:3.12-alpine

WORKDIR /app

COPY ngrok_quick/ ./ngrok_quick
COPY pyproject.toml .
COPY README.md .

RUN python -m pip install -U pip
RUN python -m pip install .

CMD ["ngrok-quick", "run"]
