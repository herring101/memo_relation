#!/bin/bash

# Get the current date and time
datetime=$(date '+%Y%m%d%H%M%S')

# The directory where the markdown files will be stored
dir="${PWD}/docs"

# Create a new markdown file with the current date and time
touch "${dir}/${datetime}.md"

# Open the new file in VSCode
code "${dir}/${datetime}.md"
