#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods
curl -sI "$1" | grep -i 'allow' | cut -c 8-
