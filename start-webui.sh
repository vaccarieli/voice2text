#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: $0 <path>"
    exit 1
fi

# Accept the path as an argument
PATH_TO_VENV="$1"

# Check if the virtual environment exists
if [ ! -d "$PATH_TO_VENV" ]; then
    echo "Virtual environment not found at: $PATH_TO_VENV"
    exit 1
fi

source "$PATH_TO_VENV/bin/activate"

PYTHON="$PATH_TO_VENV/bin/python"
echo "Using Python from virtual environment: $PYTHON"
echo ""

# Assuming your Python script is named app.py, you can pass additional arguments if needed
python app.py "${@:2}"

deactivate
