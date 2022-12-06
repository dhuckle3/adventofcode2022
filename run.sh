#!/bin/sh

source bin/activate

pip install -r requirements.txt

python -m black src

python src/day00/solution.py
python src/day01/solution.py
python src/day02/solution.py
python src/day03/solution.py
python src/day04/solution.py
python src/day05/solution.py
