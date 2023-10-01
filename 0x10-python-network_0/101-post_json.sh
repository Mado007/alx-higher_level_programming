#!/bin/bash
# script takes URL and sends a request to that URL and displays size of the body of the response.
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
