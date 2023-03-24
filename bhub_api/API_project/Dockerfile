FROM python:3.9.5

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY Pipfile.lock .

RUN pipenv install requests

COPY . .

EXPOSE 8000

CMD ["python","manage.py","runserver"]