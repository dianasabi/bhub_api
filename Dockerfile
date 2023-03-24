# syntax=docker/dockerfile:1
ARG PYTHON_VERSION=3.9.5
FROM  python:$PYTHON_VERSION-slim

WORKDIR /bhub_api
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver]
