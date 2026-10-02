#!/bin/bash
set -e

echo "Setting up the environment..."

#Create the virtual environment
python3 -m venv venv
source venv/bin/activate

#Install the required dependencies
pip install -r requirements.txt

echo "Environment setup complete."

