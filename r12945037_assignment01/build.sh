# environment building
#!/bin/bash
echo "Creating virtual environment..."
python3 -m venv venv

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
pip install --upgrade pip
pip install sqlite3 argparse

echo "Environment is set up. To activate the environment, run: source venv/bin/activate"
