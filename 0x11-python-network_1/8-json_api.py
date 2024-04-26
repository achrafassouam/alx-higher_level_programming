#!/usr/bin/python3
"""
Write a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
from sys import argv


if __name__ == "__main__":
    letter = argv[1] if len(argv) > 1 else ""

    url = "http://0.0.0.0:5000/search_user"

    data = {'q': letter}

    try:
        response = requests.post(url, data=data)

        json_data = response.json()

        if json_data:
            user_id = json_data.get('id')
            user_name = json_data.get('name')
            print("[{}] {}".format(user_id, user_name))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e.code))
