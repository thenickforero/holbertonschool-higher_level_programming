#!/usr/bin/python3
"""Script that lists the latest 10 commits of a repository from certain user
and prints the SHA id and the author of the commit.
"""
from sys import argv
from requests import get


if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'
    (repo, owner) = argv[1:3]

    response = get(url.format(owner, repo))
    data = response.json()
    for commit in data[:10]:
        sha_sum = commit.get("sha")
        author = commit.get("commit").get("author").get("name")
        print("{}: {}".format(sha_sum, author))
