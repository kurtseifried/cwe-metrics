#!/bin/bash

cd data

rm 699-software-summary-data.csv

echo "Year,Month,Count" > 699-software-summary-data.csv

csvcut -c Submission_ReleaseDate 699-summary.csv | tail -n +2 | sed 's/-[0-9][0-9]$//' | sed 's/-/,/' | sort | uniq -c | awk -F" " '{print $2","$1}' >> 699-software-summary-data.csv

