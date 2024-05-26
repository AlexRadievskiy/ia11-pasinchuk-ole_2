FROM python:3.8-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y gcc default-libmysqlclient-dev pkg-config netcat-openbsd

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app

CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8000"]
