#!/bin/bash
# FILE=/usr/local/bin/urban
FILE=/usr/local/bin/urban
if test -f "$FILE"; then
    echo "Error! $FILE already exists."
else
    echo "Installing..."
    cp src/urban.py $FILE
    echo "done"

fi
