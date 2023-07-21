#!/bin/bash

# The file to process
file=$1

# The directory of the python scripts
dir="${PWD}/src/pysrc"

# Run the Python script to calculate the embeddings and save them in HDF5
python "${dir}/embeddings.py" "${file}"
