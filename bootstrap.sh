#!/bin/sh
export FLASK_APP=./spork/index.py
source $(pipenv --venv)/bin/activate
flask run -h localhost -p 8080