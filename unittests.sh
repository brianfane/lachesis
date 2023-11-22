#!/bin/bash

# pip install --upgrade .
pip install .
cd ..

python -m unittest discover lachesis
