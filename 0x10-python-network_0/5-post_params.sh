#!/bin/bash
# POST request to the passed URL, and displays the body of the response w 2 variables
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
