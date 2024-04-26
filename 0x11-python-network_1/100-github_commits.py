#!/usr/bin/python3
"""
Python script that takes your GitHub credentials
and uses the GitHub API to display your id
"""

from sys import argv
import requests


if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(repo, owner)

    response = requests.get(url)

    try:
        if response.status_code == 200:
            commits = response.json()
            for commit in commits[:10]:
                sha = commit.get('sha')
                author_name = commit.get('commit').get('author').get('name')
                print("{}: {}".format(sha, author_name))
        else:
            print("Error fetching commits.")
            print("Status code: {}".format(response.status_code))
    except IndexError:
        pass
