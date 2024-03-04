#!/bin/bash

cd data

rm -f 699.csv.zip
rm -f 1194.csv.zip
rm -f 1000.csv.zip

rm -f 699.csv
rm -f 1194.csv
rm -f 1000.csv

wget https://cwe.mitre.org/data/csv/699.csv.zip 
wget https://cwe.mitre.org/data/csv/1194.csv.zip
wget https://cwe.mitre.org/data/csv/1000.csv.zip

unzip 699.csv.zip
unzip 1194.csv.zip
unzip 1000.csv.zip

rm -f 699.csv.zip
rm -f 1194.csv.zip
rm -f 1000.csv.zip
