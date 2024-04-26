#!/usr/bin/python3
"""
Write a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    access_token = argv[2]

    url = "https://api.github.com/user"

    headers = {
        "Authorization": "token {}".format(access_token)
    }

    try:
        response = requests.get(url, headers=headers)
        user_data = response.json()
        user_id = user_data.get('id')
        print("{}".format(user_id))
    except ValueError:
        print("Not a valid JSON")
    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
