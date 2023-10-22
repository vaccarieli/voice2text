#!/bin/bash

read -p "Path to the file(s) you want to process: " input_path
if [ -z "$input_path" ]; then
    echo "You did not provide a path. Exiting."
    read -p "Press Enter to continue..."
    exit
fi

activate_venv() {
    PYTHON="./venv/bin/python"
    echo "venv $PYTHON"
}

activate_venv
launch() {
    $PYTHON app.py --path "$input_path"
    read -p "Press Enter to continue..."
    exit
}

launch
