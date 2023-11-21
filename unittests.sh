#!/bin/bash

pip install --upgrade .
cd ..

python -m unittest discover lachesis
