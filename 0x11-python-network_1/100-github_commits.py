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
    commits = response.json()

    try:
        for commit in range(10):
            print("{}: {}".format(
                commits[commit].get("sha"),
                commits[commit].get("commit").get("author").get("name")))
    except IndexError:
        pass
