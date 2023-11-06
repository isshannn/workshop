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

## Validations
[X] Ensure that you only save the CSV files and not the ZIP files.
[X] Ensure that the date entered by the user is correct
    - Only valid date format is accepts. And the date format should be DD/MMM/YYYY
[X] Ensure that you do not fetch data for weekends
    - Bhavcopy files are available only for weekdays.
[X] Ensure that you do not fetch data for NSE holidays
    - NSE holidays are market close days and bhavcopy is not available
    - [Holiday List](https://groww.in/p/nse-holidays)
[X] Ensure that you do not fetch files that are already existing
    - There is no point re-downloading a file that already exists
[X] Ensure that you do not attempt to download the same-day bhavcopy before 7 PM.
    - Bhav copy is made available after the end of the day; typiccally after 6.30 PM.

### Bhavcopy file format
Within each file (or bhavcopy) the data is arranged in CSV format and each column is fixed. I will explain the inner-details in coming week(s)

## Comments on code 
1. [X] Each method/function should have a documentation in the format as prescribed by Python documentation and best practices.
2. [] In the file_downloader function, perform basic sanity of the correctness of the URl before calling the requests.get method. You can use an open-source library to perform that validations. (Do not handcode the validations of the url.)
    - urllib.parse was implemented but currently commented for future usuage
3. [X] Incorporate exception handling by using `try-except` blocks in the file_downloader function. That's always a good idea to write defensive code!
4. [X] Cuurently every file is downloaded as `download.zip`. Please give each downloaded file a unique name; for example, you can use the bhav file name as-it-is.
5. [X] Currently, file_check is not used (before downloading the file). Please use this method before actual download to avoid duplicate downloads!
6. [ ] 

## Parking Lot
[ ] Print betterment - Method name followed by variable name followed by variable
    - need to explore a open source logger
[X] Doc Strings - write documentations for each methods 

[ ] remove unit test warning for file open

[ ] invalidate date input of year < 2018

[X] Download files for a given month
    - unittest not implemented

[] Download files for a given year
    - unittest not implemented

## Questions

1. How do you operate with dates in Python?
Ans: Look for an external python library from internet.

2. After opening the file, how do you unzip it, and in case of error handling how do you show it?   
Ans: Look for an external python library from internet.

3. do we write set up and tear down function inside a class?
Ans: Refer to the online examples on the net.

4. try except

5. NSE monthly file available?

6. Instead of using loops for extracting individual dates, is there any method to check valid dates and months?
Ans: You need to handcode the dates and months; There is no automated way

7. On that note are datetime objects mutable?
Ans: read documnetation.