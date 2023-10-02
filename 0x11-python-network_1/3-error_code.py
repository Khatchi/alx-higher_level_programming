#!/usr/bin/python3
"""
A script that sends a request to a given URL and displays the response body.
Usage: ./3-error_code.py <URL>
  - As well as handles HTTP errors.
"""
import urllib.error
import urllib.request
import sys


if __name__ == "__main__":

    url = sys.argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
