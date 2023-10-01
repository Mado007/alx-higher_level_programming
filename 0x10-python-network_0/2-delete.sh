#!/bin/bash
# script takes URL and sends a request to that URL and displays size of the body of the response.
# -X DELETE sends a DELETE request to the URL
curl -s "$1" -X DELETE
