#!/usr/bin/python3
"""Sends a request to a URL and displays the X-Request-Id header value."""
import sys 
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.getheader("X-Request-Id"))
