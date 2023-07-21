#!/bin/bash

for file in docs/*.md; do
    python src/pysrc/embeddings.py "$file"
done
