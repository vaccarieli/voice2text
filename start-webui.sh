#!/bin/bash

source venv/bin/activate

PYTHON="venv/bin/python"
echo "venv ${PYTHON}"

while true; do
    python app.py $*          # Start a new Python process
    pkill -f "python app.py"  # Terminate the running Python process
    wait                      # Wait for the process to finish
done

deactivate
