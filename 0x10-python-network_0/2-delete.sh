#!/bin/bash
# A bash script that sends a DELETE request to the URL passed as the first arg. and displays the body of the response.
curl -sX DELETE "$1"
