import requests
from zipfile import ZipFile
from datetime import date,datetime
import os
from constants import BASE_DIR, NSE_HOLIDAYS, BASE_URL
from urllib.parse import urlparse

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

def check_month(argument):
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
    if(argument):
        #Checks if the input is whole number
        if(argument.isdecimal()):
            m = int(argument)
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
    argument: datetime.date
        Is datetime.date object which has local date and time in it
    
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

def verify_date(argument):
    """Checks validity of a date
        This function takes a date and verifies wether the date is valid or not(weekends, NSE holidays are invalid). Also, for the current date time shouldn't be before 7:00pm/19:00hrs for a valid date

    Parameters: 
    -----------
    argument: datetime.date
        Date for which the validity check needs to be done

    Returns: 
    --------
    None or datetime.date
        None if the date is invalid else return the argument
    """
    if(argument):
        t_date =  date.today()
        #Checks for Holidays
        for i in range(0 , len(NSE_HOLIDAYS)):
            if ( argument == NSE_HOLIDAYS[i] ):
                print("Holiday, Market closed")
                return None                
        #Checks for Weekend
        if(argument.strftime("%w") == "6" or argument.strftime("%w") == "0"):
            print("Weekend, Market Closed")
            return None
        #Checks for future date
        if (t_date < argument):
            print("Not available yet for this date")
            return None
        #Checks for same date
        if (t_date == argument):
            time_now = datetime.now()
            if( check_time(time_now)):
                print("Work in progress, kindly wait till 7:00pm / 19:00hrs")
                exit(0)
            else:
                return argument
        #Checks for previous date
        if(t_date > argument):
            return argument
    return None

def compose_file_path(argument):
    """Returns a string which contains file path for the input date
        This function creates a unique file for input date. Returns None if a file of the corresponding date exists in the system

    Papameters:
    -----------
    argument : datetime.date
        is a datetime.date input which contains the input date

    Returns:
    --------
    None if file already exists in system
    str if the filepath is created succesfully
    """
    #Checks if preexisting file exists  
    file_path = "/cm" + argument.strftime("%d") + argument.strftime("%b").upper() + argument.strftime("%Y") +"bhav.csv"
    if check_file((file_path)):
        print("File exists")
        return None
    file_path = file_path.lstrip("/")
    file_path = file_path.rstrip(".csv")
    # Add a character, since rstrip messes with the file name Bhav
    file_path = file_path + "v.zip"
    return file_path
    # print(file_path)
    # download_file(file_url,file_path)

def download_file(url,argument):
    """Helper function to download a file for a given url. 
        This function takes a url and a string argument which is a file path, returns True if a file download is successful or None if it fails.

    Parameters:
    -----------
    url: str
        A string which contains the url of the file to be downloaded. For each date the url is unique
    
    argument: str
        A string which contains the path to which the downloaded file is unzipped and stored at
    
    Returns:
    --------
    None or True
        None if the file download fails else returns None if download fails.
    """
    if (url):
        print("URL to download: [", url, "]")
        try:
            res = requests.get(url, allow_redirects=True)
        except Exception as e:
            print("There is an error in services as follows: ", e)
            return None
        finally:
            # print("Server down. Please try again later")
            pass
        # Note that the address is fetched automatically from constants.py
        f = open(os.path.join(BASE_DIR,argument), 'wb').write(res.content)
        # the adresses here point to the zip file downloaded and to where it's extracted
        print("BASE_DIR: [", BASE_DIR, "]")
        print("file [", os.path.join(BASE_DIR,argument), "]")
        with ZipFile(os.path.join(BASE_DIR,argument), "r") as unzip:
            unzip.extractall(path=BASE_DIR)
        if (os.path.exists(os.path.join(BASE_DIR,argument))):
            os.remove(os.path.join(BASE_DIR,argument))
        return True
    print("None Value passed")
    return None

def check_file(argument):
    """Checks if the of file already exists in the system
        This function takes the file name as a string input and verifes wether the file is present in system or not. If it is present returns True. If it's not returns False.
        
    Parameters:
    -----------
    argument: str
        File name.
    
    Returns:
    --------
    None or int
        None if the input is not a Decimal number \n
        None if input > 31 or input < 0 or input == None \n
        int if input>0 and input<32  
    """
    if(argument):
        argument = BASE_DIR + argument
        if(os.path.exists(argument)):
            return True
        else:
            return False    

def compose_url(argument):
    """Creates a url for an given date
        This function take a date as input and returns a string which contains the url reuired to download the file for the corresponding date

    Parameters:
    -----------
    argument: datetime.date
        Date for which the url is to be created.
    
    Returns:
    --------
    None or str
        None if the argument passed is None, else str.

    """
    if(argument):
        # creates URL based on the date
        file_url = BASE_URL + argument.strftime("%Y") + "/" + argument.strftime("%b").upper() + "/cm" + argument.strftime("%d") + argument.strftime("%b").upper() + argument.strftime("%Y") +"bhav.csv.zip"
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
            for d in range(1,31):
                current_date = date(year,month,d)
                current_date = verify_date(current_date)
                if ( current_date != None):
                    try:
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

def process_input():
    print("Do you want to fetch files for a single date or for a range?")
    print("1: Single day")
    print("2: Range")
    c = input()
    c = int(c)
    match c:
        case 1:  
            print("Enter Date")
            dd = input()
            # dd = "2"
            dd = check_day(dd)
            if(dd == None):
                exit(0)

            print("Enter Month")
            mm = input()
            # mm = "11"
            mm = check_month(mm)
            if(mm == None):
                exit(0)

            print("Enter Year")
            # yy = "2023"
            yy = input()
            yy = check_year(yy)
            if(yy == None):
                exit(0)

            #stores the date input by the user
            input_date = date(yy,mm,dd)
            input_date = verify_date(input_date)
            if(input_date == None):
                exit(0)
            try:
                url = compose_url(input_date)
                file_path = compose_file_path(input_date)
            except Exception as e:
                print("The following error occured: \n ",)

        
    
        case 2: 
            print("Enter start day")
            sd = input()
            sd = check_day(sd)
            sd = int(sd)

            if (sd == None):
                exit(0)

            print("Enter start month")
            sm = input()
            sm = check_month(sm)
            sm = int(sm)

            if (sm == None):
                exit(0)

            print("Enter start Year")
            sy = input() 
            sy = check_year(sy)
            sy = int(sy)

            if (sy == None):
                exit(0)

            print("Enter end day")
            ed = input()
            ed = check_day(ed)
            ed = int(ed)

            if (ed == None):
                exit(0)

            print("Enter end month")
            em = input()
            em = check_month(em)
            em = int(em)

            if (em == None):
                exit(0)

            print("Enter end Year")
            ey = input()
            ey = check_year(ey)
            ey = int(ey)

            if (ey == None):
                exit(0)

            try:
                start_date = date(sy,sm,sd)
                end_date = date(ey,em,ed)
            except Exception as E:
                print("The following error occured: \n ", E)

            td = date.today()
            if (end_date > td):
                print("Data not available for future dates. Kindly fecth data on or before "+ td.strftime("%d %m %Y"))
                exit(0)

        # print(start_date," ",end_date)

            for y in range(sy,ey+1):
            # print("Program on sleep for 5 seconds")
            # print(start_date," ",end_date,"/n")
            # time.sleep(5.0)
                for m in range(sm,13):
                    for d in range(sd,32):
                        try:
                            if(start_date == end_date):
                            # print("Done")
                                break
                            start_date =date(sy,m,d)

                            print(start_date)
                            if(d==31):
                                if(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
                                    sm=sm+1
                            if(d==30):
                                if(m==4 or m==6 or m==9 or m==11):
                                    sm=sm+1
                            if(d==28 and sy%4!=0):
                                if(m==2):        
                                    sm = sm+1
                            if(d==29 and sy%4==0):
                                if(m==2):
                                    sm=sm+1
                            if(m == 12 and d == 31):
                                sm = 1
                                sy = sy + 1
                            if(d == 31):
                                sd = 1   
                        except:
                            continue

# process_input()