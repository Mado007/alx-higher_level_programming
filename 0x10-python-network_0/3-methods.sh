#!/bin/bash
# script takes URL and sends a request to that URL and displays size of the body of the response.
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -f2- -d" "
