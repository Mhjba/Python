#!/bin/bash
# displays the body of the response.
curl -sX POST -H "Content-Type: application/json" -d "@$2" "$1"
