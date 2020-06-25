from python:3

MAINTAINER Shravankumar Nagarajan

COPY . /app
WORKDIR /app

RUN pip install pipenv

RUN pipenv install --system --deploy --skip-lock

CMD ["python", "run.py"]