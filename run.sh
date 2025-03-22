#!/bin/bash

echo "Activating virtual environment..."
source venv/bin/activate

echo "Running the Marketplace CLI application..."
python main.py "$@"

deactivate
