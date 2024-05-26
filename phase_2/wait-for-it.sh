#!/usr/bin/env bash
#   Use this script to test if a given TCP host/port are available

set -e

HOST=$1
PORT=$2
shift 2
CMD="$@"

if [ -z "$HOST" -o -z "$PORT" ]; then
  echo "Usage: $0 host port [cmd...]" >&2
  exit 1
fi

while ! nc -z $HOST $PORT; do
  echo "Waiting for $HOST:$PORT..."
  sleep 1
done

exec $CMD
