# About
This project aims to scrap csv data(Bhavcopy file) from the website "https://www.nseindia.com/all-reports" (denoted as bhav_copy) and manipulate the fetched data as and per end user requirements.

# Current Status of the project
The api of the project is under construction and not fully implemented. The stand-alone python codes are unittested and are able to download and store daily,weekly,montly and yearly bhav_copy.
Separate .csv files of listed companies can be created for weekly reports. Top Gainers and loosers of the week can be displayed.

# Walkthrough
Weekly Progress are documentated in folders week_**. Standalone code and api is present inside the folder "code". Folders with lable practise are dummy folders for code trials and can be ignored for the purpose of the project. 

# Dependencies
[1] Python 3.10 and higher
[2] Pandas
[3] Flask
[4] Flask_restful
[5] urlparse
[6] zipfile

# Future Features
[ ] A full fleged api with flexible data manipulation wrt any input time period.
[ ] A website with for simpler UI.