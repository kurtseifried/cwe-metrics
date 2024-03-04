#!/bin/bash

cd data

rm -f 699-summary.csv
rm -f 1000-summary.csv
rm -f 1194-summary.csv

dos2unix *

../generate-csv-data.py 699.xml 699-summary.csv
../generate-csv-data.py 1000.xml 1000-summary.csv
../generate-csv-data.py 1194.xml 1194-summary.csv

