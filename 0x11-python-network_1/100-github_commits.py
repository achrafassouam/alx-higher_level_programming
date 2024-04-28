#!/usr/bin/python3
"""
Python script that takes your GitHub credentials
and uses the GitHub API to display your id
"""

from sys import argv
import requests

if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        argv[1], argv[2]
    )
    para = {'per_page': 10}
    response = requests.get(url, params=para)
    commits = response.json()
    for commit in commits:
        sha = commit.get('sha')
        author_name = commit.get('commit').get('author').get('name')
        print("{}: {}".format(sha, author_name))
