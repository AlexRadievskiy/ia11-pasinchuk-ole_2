FROM python:3.8-slim
WORKDIR /app

RUN apt-get update && \
    apt-get install -y gcc default-libmysqlclient-dev pkg-config netcat-openbsd mongodb-clients

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

COPY . /app
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]
