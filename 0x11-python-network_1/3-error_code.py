#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the response
"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            print(content)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
