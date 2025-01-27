#!/bin/bash

echo "$(date) : START"
echo "$(date) : Create conda env using Python 3.8"
conda create --prefix ./env python=3.8s -y

echo "$(date) : Activate conda env"
source ./env/bin/activate  # Use this for Unix-based systems (Linux/MacOS)
# For Windows, use: conda activate ./env

echo "$(date) : Install dev requirements"
pip install -r requirements_dev.txt

echo "$(date) : END"
