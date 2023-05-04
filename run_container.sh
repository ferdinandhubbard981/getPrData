#!/bin/bash

if [ "$#" -ne 4 ]; then
    echo "Usage: ./run_container.sh <repo> <since_date> <access_token> <output_file>"
    exit 1
fi

REPO=$1
SINCE_DATE=$2
ACCESS_TOKEN=$3
OUTPUT_FILE=$4

docker run --rm -v "$(pwd)":/app/output fetch_prs python getPrData.py --repo "$REPO" --since_date "$SINCE_DATE" --access_token "$ACCESS_TOKEN" --output_file "output/$OUTPUT_FILE"
