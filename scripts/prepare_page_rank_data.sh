#!/usr/bin/env bash

# WARNING: Only tested in MacOS.

# Prep
rm -fr datasets/openpagerank/*
mkdir -p datasets/openpagerank
cd datasets/openpagerank


echo 'Fetching OpenPage rank data...'
curl -O 'https://www.domcop.com/files/top/top10milliondomains.csv.zip'
unzip top10milliondomains.csv.zip


echo 'Removing header row from CSV...'
sed '1d' top10milliondomains.csv > tmpfile
rm top10milliondomains.csv


echo 'Extracting domain column from CSV... (this may take a short while)'
cut -f 2 -d, tmpfile > top_tenmillion_domains.csv
rm tmpfile
awk '{gsub(/\"/,"")};1' top_tenmillion_domains.csv > top_tenmillion_domains_cleaned.csv
mv top_tenmillion_domains_cleaned.csv top_tenmillion_domains.csv


echo 'Creating reduced list files...'
head -n 1000000 top_tenmillion_domains.csv > top_million_domains.csv
head -n 1000 top_tenmillion_domains.csv > top_thousand_domains.csv


echo "Files created and ready"
echo "Line count:" $(wc -l top_thousand_domains.csv)
echo "Line count:" $(wc -l top_million_domains.csv)
echo "Line count:" $(wc -l top_tenmillion_domains.csv)
