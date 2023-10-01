#!/bin/bash
# script takes URL and sends a request to that URL and displays size of the body of the response.
curl -s "$1" -H "X-School-User-Id: 98"
