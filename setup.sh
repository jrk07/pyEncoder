#!/bin/bash

MAIN_DIR="videos"
SUBDIR1="to_be_processed"
SUBDIR2="processed"

if [ ! -d "$MAIN_DIR" ]; then
    mkdir "$MAIN_DIR"

    if [ ! -d "$MAIN_DIR/$SUBDIR1" ]; then
        mkdir "$MAIN_DIR/$SUBDIR1"
        echo "Subdirectory '$SUBDIR1' created inside '$MAIN_DIR'."
    fi

    if [ ! -d "$MAIN_DIR/$SUBDIR2" ]; then
    mkdir "$MAIN_DIR/$SUBDIR2"
    echo "Subdirectory '$SUBDIR2' created inside '$MAIN_DIR'."
    fi
    echo "All necessary directories created."
else
    echo "All necessary directories already exist."
fi