#!/usr/bin/env bash

HOST=$1
PORT=$2

while ! nc -z $HOST $PORT; do
  echo "Waiting for $HOST:$PORT..."
  sleep 1
done

echo "$HOST:$PORT is available!"
