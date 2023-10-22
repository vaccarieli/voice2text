#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <input_path>"
    exit 1
fi

input_path="$1"

activate_venv() {
    PYTHON="./venv/bin/python"
    echo "venv $PYTHON"
}

activate_venv

launch() {
    $PYTHON app.py --path "$input_path"
    exit
}

launch
