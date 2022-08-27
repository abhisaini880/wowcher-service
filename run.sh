#!/bin/bash

if [[ -f "/proc/cpuinfo" ]]
then
    # This will be used in production to utilize the cpu resources available in the server
    source venv/bin/activate
    pip3 install -r requirements.txt
    gunicorn app.main:app -b :8000 -k uvicorn.workers.UvicornWorker --workers $(( 2 * `cat /proc/cpuinfo | grep 'core id' | wc -l` + 1 )) --error-logfile - --log-level info
else
    # For development purposes only
    # Run below command in terminal to install event broker
    # source .env
    # poetry run uvicorn app.main:app --port 5000 --reload
    source venv/bin/activate
    pip3 install -r requirements.txt
    uvicorn app.main:app --port 8000 --reload
fi
