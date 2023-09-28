#!/bin/bash
# script takes URL and sends a request to that URL and displays size of the body of the response.
# -I displays the header information
curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2
