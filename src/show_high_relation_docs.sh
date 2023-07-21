#!/bin/bash

# The file to process
file=$1

# The directory of the python scripts
dir="${PWD}/src/pysrc"

# Run the Python script to calculate the embeddings
python "${dir}/calc_relation.py" "${file}"