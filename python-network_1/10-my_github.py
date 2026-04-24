#!/usr/bin/python3
"""Displays GitHub user id using Basic Authentication."""
import sys
import requests


if __name__ == "__main__":
    user = sys.argv[1]
    token = sys.argv[2]

    r = requests.get("https://api.github.com/user", auth=(user, token))
    print(r.json().get("id"))
