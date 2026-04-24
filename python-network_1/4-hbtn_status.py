#!/usr/bin/python3
"""Fetches status from intranet using requests."""
import requests


if __name__ == "__main__":
    r = requests.get("https://intranet.hbtn.io/status")
    body = r.text

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
