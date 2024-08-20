#!/bin/bash

# Directory containing the folders
base_directory="/Users/jcbecker/Documents/GitHub/LP890-9_2/TidalEarth/ParameterSweep"

# Loop through each item in the base directory
for dir in "$base_directory"/*/; do
  if [ -d "$dir" ]; then
    echo "Entering directory: $dir"
    cd "$dir" || exit
    vplanet vpl.in
    cd "$base_directory" || exit
  fi
done

echo "Finished processing all directories."

