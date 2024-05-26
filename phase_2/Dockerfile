FROM python:3.8-slim

RUN apt-get update && \
    apt-get install -y gcc default-libmysqlclient-dev netcat-openbsd

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

COPY . /app

CMD ["/wait-for-it.sh", "db:27017", "--", "python", "manage.py", "runserver", "0.0.0.0:8000"]
