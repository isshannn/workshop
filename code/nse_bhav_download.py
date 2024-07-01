import requests
from zipfile import ZipFile
from datetime import date,datetime
import os
from constants import BASE_DIR, NSE_HOLIDAYS, BASE_URL
# from urllib.parse import urlparse

def check_day(argument):
    """Checks the validity of day entered
        This function takes a string as input and verifes wether the input is valid day or not. If it is valid returns day as integer. If it fails then returns None

    Parameters:
    -----------
    argument: str
        Is a user input for day. Should be a whole number
    
    Returns:
    --------
    None or int
        None if the argument is not a Decimal number \n
        None if argument > 31 or argument < 0 or argument == None \n
        int if argument > 0 and argument <32  
    """
    if(argument):
        #Checks if the input is whole number
        if(argument.isdecimal()):
            d = int(argument)
            #Checks for Valid Day input
            if( d>0 and d<32):
                return d
            else:
                print("Enter a date between 1 to 31")
                return None
        print("Enter a date between 1 to 31")    
        return None
    print("None Value passed")
    return None

def check_month(month_number = str):
    """Checks the validity of month entered
        This function takes a string as input and verifes wether the input is valid month or not. If it is valid returns month as integer. If it fails then returns None

    Parameters:
    -----------
    argument: str
        Is a user input for month. Should be a whole number
    
    Returns:
    --------
    None or int
        None if the argument is not a Decimal number \n
        None if argument > 12 or argument < 0 or argument == None \n
        int if argument < 13 and argument > 0  
    """
    if(month_number):
        #Checks if the input is whole number
        if(month_number.isdecimal()):
            m = int(month_number)
            #Checks if the input is a valid month number
            if(m>0 and m < 13):
                return m;
            else:
                print("Enter a valid month number between 1 to 12")
                return None
        print("Enter a valid month number between 1 to 12")    
        return None
    print("None Value Passed")
    return None   

def check_time(argument):
    """Checks if time is less then 7:00pm/19:00hrs
        This function returns true if the current local time is less then 7:00pm/19:00hrs
    
    Parameters:
    -----------
    argument: datetime.datetime
        Is datetime.datetime object which has local date and time in it
    
    Returns:
    --------
    True if time is less then 7:00pm/19:00hrs
    False if time is greater than 7:00pm/19:00hrs
    """
    if(argument):
        time_now = argument.strftime("%H")
        time_now = int(time_now)
        if (time_now < 19):
            return True
        else:
            return False

def check_year(argument):
    """Checks the validity of year entered
        This function takes a string as input and verifes wether the input is valid year or not(Years in future are invalid, Year expressed in words are invalid). If it is valid returns year as integer. If it fails then returns None

    Parameters:
    -----------
    argument: str
        Is a user input for Year. Should be a whole number
    
    Returns:
    --------
    None or int
        None if the argument is not a Decimal number \n
        None if argument == None \n
        None if argument entered is in future. for example giving argument as 2024 when the current date is 20/10/2023; \n
        None if argument < 2018
        int if argument is a year in past or present
    """
    if(argument):
        #Check if the input is whole number
        if(argument.isdecimal()):
            y = int(argument)
            #Fecthes the present year
            td = date.today()
            td = td.strftime("%Y")
            td = int(td)
            #Checks if the input year is ongoing or not.
            if (y > td):
                print("Enter ongoing or past year")
                return None
            if (y < 2018):
                print("Cannot fetch data for years less than 2018")
                return None
            return y
        print("Enter year in whole numbers, eg. 2011")
        return None
    print("None value passed")
    return None    

def verify_date(input_date: date):
    """Checks validity of a date
        This function takes a date and verifies wether the date is valid or not(weekends, NSE holidays are invalid). Also, for the current date time shouldn't be before 7:00pm/19:00hrs for a valid date

    Parameters: 
    -----------
    sample_date: datetime.date
        Date for which the validity check needs to be done

    Returns: 
    --------
    None or datetime.date
        None if the date is invalid, or falls on a listed holiday, or on a weekend \n
        False if the date is in future, or the csv_data for the current date isnt made yet \n
        The input date if the input is a valid date
    """
    if (input_date):
        today_date =  date.today()
        #Checks for future date
        if (today_date < input_date):
            print("verify_date :: Kindly wait until the market resumes at 9:00 hrs IST on ", input_date)
            return False
        #Checks for Holidays
        if input_date in NSE_HOLIDAYS:
            print("verify_date :: Holiday, Market closed on ", input_date)
            return None 
        
        # for i in range(0 , len(NSE_HOLIDAYS)):
        #     if (NSE_HOLIDAYS[i] > input_date):
        #         break
        #     if ( input_date == NSE_HOLIDAYS[i] ):
        #         print("verify_date :: Holiday, Market closed on ", input_date)
        #         return None                

        #Checks for Weekend
        if(input_date.strftime("%w") == "6" or input_date.strftime("%w") == "0"):
            print("verify_date :: Weekend, Market Closed on ", input_date)
            return None
        #Checks for same date
        if (today_date == input_date):
            time_now = datetime.now()
            if( check_time(time_now)):
                print("verify_date :: Work in progress, kindly wait till 7:00pm / 19:00hrs")
                return False
            else:
                return input_date
        #Checks for previous date
        if(today_date > input_date):
            return input_date
    return None

def compose_file_path(sample_date):
    """Returns a string which contains file path for the input date
        This function creates a unique file(.zip) for input date. Returns None if a file of the corresponding date exists in the system

    Papameters:
    -----------
    sample_date : datetime.date
        is a datetime.date input which contains the input date

    Returns:
    --------
    str : 
        if the filepath is created succesfully
    """ 
    if(sample_date):
        file_path = "/cm" + sample_date.strftime("%d") + sample_date.strftime("%b").upper() + sample_date.strftime("%Y") +"bhav.zip"
        return file_path
    else:
        return None


def download_file(url,file_name):
    """Helper function to download a file for a given url. This function takes a url and a string argument which is a file path, returns True if a file download is successful or None if it fails.

    Parameters:
    -----------
    url: str
        A string which contains the url of the file to be downloaded. For each date the url is unique
    
    file_name: str
        A string representing the name of the csv file.
    
    Returns:
    --------
    None or True
        None if the file download fails/File exists; else returns True.
    """
    if (url):
        # if check_file(file_path):
        #     print("File Exists")
        #     return None
        print("download_file :: URL to download= [", url, "]")
        try:
            res = requests.get(url, allow_redirects=True,timeout=5.00)
        except Exception as e:
            print("download_file :: There is an error in services as follows: ", e)
            return None
        finally:
            # print("Server down. Please try again later")
            pass
        # Note that the address is fetched automatically from constants.py
        file_name = file_name.lstrip("/")
        f = open(os.path.join(BASE_DIR,file_name), 'wb').write(res.content)
        # the adresses here point to the zip file downloaded and to where it's extracted
        print("BASE_DIR: [", BASE_DIR, "]")
        print("file [", os.path.join(BASE_DIR,file_name), "]")
        with ZipFile(os.path.join(BASE_DIR,file_name), "r") as unzip:
            unzip.extractall(path=BASE_DIR)
        if (os.path.exists(os.path.join(BASE_DIR,file_name))):
            print("download_file: Removing path= ",os.path.join(BASE_DIR,file_name))
            os.remove(os.path.join(BASE_DIR,file_name))
        return True
    print("download_url :: None Value passed")
    return None

def check_file(csv_file_name = str):
    """Checks if the csv file already exists in the system
        This function takes the file name(.csv without full path) as a string input 
        and verifes wether the file is present in system or not. 
        If it is present returns True. If it's not returns False.
        
    Parameters:
    -----------
    argument: str
        File name in CSV format
    
    Returns:
    --------
    True 
        If the file exists in ./bhav_copy folder
    False
        If the file doesnt exist. 
    """
    if(csv_file_name):
        if(csv_file_name.endswith(".zip")):
            csv_file_name = csv_file_name.rstrip("zip")
            csv_file_name = csv_file_name + "csv"
            csv_file_name = csv_file_name.lstrip("/")
        if (os.path.isfile(os.path.join(BASE_DIR, csv_file_name))):
            return True
        else:
            return False
    else:
        return None    

def compose_url(url_date):
    """Creates a url for an given date
        This function take a date as input and returns a string which contains the url reuired to download the file for the corresponding date

    Parameters:
    -----------
    url_date: datetime.date
        Date for which the url is to be created.
    
    Returns:
    --------
    None or str
        None if the argument passed is None, else str.

    """
    if(url_date):
        # creates URL based on the date
        file_url = BASE_URL + url_date.strftime("%Y") + "/" + url_date.strftime("%b").upper() + "/cm" + url_date.strftime("%d") + url_date.strftime("%b").upper() + url_date.strftime("%Y") +"bhav.csv.zip"
        # result = urlparse(file_url)
        # if(not (result.scheme and result.path)) :
        #     print("URL Error")
        #     return None
        # else:
        return file_url
    else:
        return None
    
def download_file_for_month(month, year):
    """Creates URL for every working day in a specified month,year
            Takes two string inputs for month and year respectively. Creates unique url for each valid day of the specified month

    Parameters:
    -----------
    month : str
        A string input which contains valid month in whole number

    year : str
        A string input which contains valid year in whole number

    Returns:
    --------

    None:  if month is invalid decimal number , if year is not a decimal number or is in future 

    None: if month or year or both are null/None

    Ture: if files are downloaded  

    """
    # Month cant be null
    if(month == None):
        print("compose_url_for_month: Month cant be None")
        return None    
    # Month has to be a string
    try:
        if(month.isdecimal()):
            # Integer month value cant be more than 12 and less than 1
            test_month = int(month)
            # print("compose_url_for_month: Value of Test month = ",test_month)
            if(test_month > 12 or test_month < 1):
                print("compose_url_for_month: Month number out of range")
                return None
             # if year is None then defealt year = current year
            if(year == None):
                today_year = date.today()
                today_year = today_year.strftime("%Y")
                year = today_year
                print("compose_url_for_month: None year passed. Default year is: ", year)
            # if year is passed then it cant be in future
            today_year = date.today()
            today_year = today_year.strftime("%Y")
            today_year = int(today_year)
            year_test = int(year)
            if (year_test > today_year):
                print("compose_url_for_month: Data for future year cant be fetched")
                return None
            print("compose_url_for_month: Month is string and in decimal and is within range")
            # for everyday of the month compose the url
            month = int(month)
            year = int(year)
            for d in range(1,32):
                try:
                    current_date = date(year,month,d)
                    current_date = verify_date(current_date)
                    if (current_date == False):
                        exit(0)
                    if ( current_date != None):
                        url_date = compose_url(current_date)
                        url_path = compose_file_path(current_date)
                        download_file(url_date,url_path)
                except:
                    continue   
            return True
    except Exception as E:
        print("compose_url_for_month: ", E)
        return None
   
    
        # print(current_date)
        #return current_date

def download_file_for_year(year):
    """Downloads files for an entire year
        This function take year(for ex: 2022) as input and downloads files for valid days for an entire year specified

    Parameters:
    -----------

    year : str
        The year for which the files are to be downloaded

    Returns:
    --------

    False: If year is null
    True : if files are downloaded
   
    """
    #Check if year input is in decimal
    #Check if year is not of future
    year = check_year(year)
    if(year != None):
        #If valid year then fetch files
        year = str(year)
        for x in range(1,13):
            month = str(x) 
            download_file_for_month(month,year)
        return True
    else:
        return False        