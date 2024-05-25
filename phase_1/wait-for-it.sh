#!/usr/bin/env bash
#   Use this script to test if a given TCP host/port are available

TIMEOUT=15
QUIET=0
HOST="$1"
PORT="$2"
shift 2

while getopts "qt:" opt; do
    case "$opt" in
    q) QUIET=1 ;;
    t) TIMEOUT="$OPTARG" ;;
    esac
done

if ! command -v nc > /dev/null; then
    echo 'Error: nc is not installed.'
    exit 1
fi

for i in $(seq $TIMEOUT); do
    if nc -z "$HOST" "$PORT"; then
        if [ $QUIET -eq 0 ]; then
            echo "$HOST:$PORT is available after $i seconds."
        fi
        exit 0
    fi
    sleep 1
done

echo "$HOST:$PORT is not available after $TIMEOUT seconds."
exit 1
