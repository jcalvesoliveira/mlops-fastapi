FROM python:3.11

WORKDIR /code

RUN pip install pdm

COPY pdm.lock pyproject.toml /code/

RUN pdm sync

COPY ./app /code/app

ENTRYPOINT ["pdm", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "$PORT"]