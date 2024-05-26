FROM python:3.8-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y gcc default-libmysqlclient-dev pkg-config netcat-openbsd

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

COPY . /app

CMD ["sh", "-c", "/wait-for-it.sh db:27017 -- python manage.py runserver 0.0.0.0:8000"]
