#!/usr/bin/python3
"""
This script displays the X-Request-Id header variable 
of a request to a given URL using sys and urllib.
Usage: ./1-hbtn_header.py <URL>
"""
import sys
from sys import argv
import urllib.request


if __name__ == "__main__":

    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
