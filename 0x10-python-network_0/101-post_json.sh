#!/bin/bash
# Send a JSON POST request to the specified URL
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"
