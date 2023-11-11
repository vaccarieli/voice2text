#!/bin/bash

source venv/bin/activate

PYTHON="venv/bin/python"
echo "venv ${PYTHON}"

python app.py $*          # Start a new Python process

deactivate
