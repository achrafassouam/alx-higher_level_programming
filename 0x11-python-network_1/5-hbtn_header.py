#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    response = requests.get(url)
    content = response.headers.get("X-Request-Id")
    
    print(content)
