#!/usr/bin/python3
"""POST email to URL and display response body."""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode(
        {"email": email}
    ).encode("utf-8")

    req = urllib.request.Request(url, data=data)

    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
