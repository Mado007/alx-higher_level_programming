#!/bin/bash 
# script takes URL and sends a request to that URL and displays size of the body of the response.
curl -s -L -X HEAD -w "%{http_code}" "$1"
