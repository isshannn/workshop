#!/bin/bash

# Input month number check for validity

echo "Enter month number (1-12): "
read mon_number
#echo "Number is: $mon_number"
if [ $mon_number -gt 12 ] || [ $mon_number -lt 1 ]
then
  echo "Invalid Month"
else
  echo "Valid Month"
fi

# Input day of the month

echo "Enter day of the month (1-31)"
read day_number
if [ $day_number -gt 31 ] || [ $day_number -lt 1 ]
then
    echo "Invalid day"
else
    echo "Valid day"
fi

# Input year
echo "Enter year (YYYY) :"
read year_number

#Prepare Date
my_date="$year_number/$mon_number/$day_number"
echo "from prepare_date: $my_date"

#Change month to text
mon_number=$(date -d "$my_date" '+%b')
mon_number=${mon_number^^}
echo "From change_month: $mon_number"

# Prepare CSV path 
default_csv_path="~/source/workshop/code/bhav_copy/cm$day_number$mon_number$year_number"
default_csv_path="$default_csv_path""bhav.csv"
echo $default_csv_path

base_url="https://archives.nseindia.com/content/historical/EQUITIES/$year_number/$mon_number/cm$day_number$mon_number$year_number"
download_url="$base_url""bhav.csv.zip"
echo $download_url
curl -O $download_url
unzip "cm$day_number$mon_number$year_number""bhav.csv.zip"
rm "cm$day_number$mon_number$year_number""bhav.csv.zip"

#https://archives.nseindia.com/content/historical/EQUITIES/2023/OCT/cm26OCT2023bhav.csv.zip

