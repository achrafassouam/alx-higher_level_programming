#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the response
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    try:
        response = requests.get(url)
        if response.status_code >= 400:
            print("Error code: {}".format(response.status_code))
        else:
            print(response.text)
    except request.exceptions.RequesteException as e:
        print("Error code: {}".format(e.code))
