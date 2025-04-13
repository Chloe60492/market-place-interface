# environment building
#!/bin/bash
echo "Check if Python3 is installed..."
python3 --version

echo "Installing dependencies..."
pip install --upgrade pip

echo "Environment is set up. To activate the environment, run: source venv/bin/activate"
