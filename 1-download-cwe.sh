#!/bin/bash

cd data

# Get rid of old stuff

rm -f 699.csv.zip
rm -f 1194.csv.zip
rm -f 1000.csv.zip

rm -f 699.xml.zip
rm -f 1194.xml.zip
rm -f 1000.xml.zip

rm -f 699.csv
rm -f 1194.csv
rm -f 1000.csv

rm -f 699.xml
rm -f 1194.xml
rm -f 1000.cxml

# Get files

wget https://cwe.mitre.org/data/csv/699.csv.zip 
wget https://cwe.mitre.org/data/csv/1194.csv.zip
wget https://cwe.mitre.org/data/csv/1000.csv.zip

wget https://cwe.mitre.org/data/xml/views/699.xml.zip
wget https://cwe.mitre.org/data/xml/views/1194.xml.zip
wget https://cwe.mitre.org/data/xml/views/1000.xml.zip

# Unpack and remove zips

unzip 699.csv.zip
unzip 1194.csv.zip
unzip 1000.csv.zip

unzip 699.xml.zip
unzip 1194.xml.zip
unzip 1000.xml.zip

rm -f 699.csv.zip
rm -f 1194.csv.zip
rm -f 1000.csv.zip

rm -f 699.xml.zip
rm -f 1194.xml.zip
rm -f 1000.xml.zip
