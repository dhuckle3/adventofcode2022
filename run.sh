#!/bin/sh

source bin/activate

pip install -r requirements.txt

python -m black src

python src/day00/solution.py
