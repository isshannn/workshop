# Objective
The objective of this week is centered around getting the familiarity in-depth about the Python eco-system. Starting with setting and debugging environment issues, writing slightly complex programs and writing exhaustive test-cases.

# Programming Challenge
Write a program that will fetch files from the internet and the number of files downloaded will depend upon the type of input provided by the end-user.
For example, the user may wish to download a file for a single day or may wish to download the file for an entire month/year, etc. 
## Backgraound of files under consideration
NSE publishes daily bhavcopy of the stocks (also called securities) exchanged (which is bought and sold) for each company. There is 1 bhavcopy published per day but NSE provides URL to download files for historical dates.

## URl and File Pattern
Each file or the URL for that matter follows a consistent pattern as descibed below.
- https://archives.nseindia.com/content/historical/EQUITIES/2023/OCT/cm27OCT2023bhav.csv.zip

Description of the URL format
Each file URL consists of the following pattern
- BASE_URL = https://archives.nseindia.com/content/historical/EQUITIES/
- YYYY = Year for the file, for example, 2023 above
- MMM = Month for the file, for example, OCT
- filename = name of the actual file, for example, cm27OCT2023bhav.csv.zip
    - cm - Fixed part for all file
    - DD - day of the month, for example, 27
    - MMM - Month part of the file name, for example, OCT
    - YYYY - Year part of the file name, for example, 2023

### Bhavcopy file format
Within each file (or bhavcopy) the data is arranged in CSV format and each column is fixed. I will explain the inner-details in coming week(s)

Questions

1. 

2. 

3. 

4. 


