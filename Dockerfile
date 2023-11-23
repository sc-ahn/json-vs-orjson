FROM python:3.10.13-bullseye

ENV POETRY_VERSION=1.4.0 POETRY_HOME=/poetry
ENV PATH=/poetry/bin:$PATH
RUN curl -sSL https://install.python-poetry.org | python3 -
WORKDIR /json-vs-orjson
COPY tests tests
COPY Makefile poetry.lock pyproject.toml posts.pickle start ./
RUN poetry install
CMD ["./start"]
