#!/bin/bash

# cd to script directory
cd "$(dirname "$0")" || exit 1

if [ ! -f "/app/config/vocabulary.txt" ]; then
  cp "vocabulary.txt" "/app/config/vocabulary.txt"
fi

python bot.py
