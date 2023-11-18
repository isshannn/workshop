from datetime import date
import constants as nse_constants
import nse_bhav_download as nse_downloader
import csv
import os

def make_stock_data_dict(dummy_list = list):
    """This function creates a single instance of dictionary for the list passed as the argument and appends it to a globally declared list
    
    Parameters:
    -----------
    dummy_list : list
        A list which reads data from a single row of a csv file

    Returns:
    --------
    stock_data: dict
        which contaings CSV data in a list of dictionaries format
    """
    #Creating a global list which stores list of the dictionaries containning data of a single row of a csv file
    #The idea is to create a list of csv_files represented in form of dictionaries
    # stock_data_list = []
    #A dictionary which stores data fetched from the csv_file
    stock_data = {
        "SYMBOL" : None ,
        "SERIES" : None ,
        "OPEN"  : None,
        "HIGH"  : None,
        "LOW"  : None,
        "CLOSE"  : None,
        "LAST"  : None,
        "PREVCLOSE"  : None,
        "TOTTRDQTY"  : None,
        "TOTTRDVAL"  : None,
        "TIMESTAMP"  : None,
        "TOTALTRADES"  : None,	
        "ISIN" : None
    }
    stock_data["SYMBOL"] = dummy_list[0]
    stock_data["SERIES"] = dummy_list[1]
    stock_data["OPEN"] = dummy_list[2]
    stock_data["HIGH"] = dummy_list[3]
    stock_data["LOW"] = dummy_list[4]
    stock_data["CLOSE"] = dummy_list[5]
    stock_data["LAST"] = dummy_list[6]
    stock_data["PREVCLOSE"] = dummy_list[7]
    stock_data["TOTTRDQTY"] = dummy_list[8]
    stock_data["TOTTRDVAL"] = dummy_list[9]
    stock_data["TIMESTAMP"] = dummy_list[10]
    stock_data["TOTALTRADES"] = dummy_list[11]
    stock_data["ISIN"] = dummy_list[12]
    # stock_data_list.append(stock_data)
    # print("feed _stock_data_list: stock_data_list as of now: ", stock_data_list)
    return stock_data

def read_daily_csv(csv_date = date, company_name = str):
    """Helper Function which reads a single bhav_CSV file for the specified Date
    
    Parameters:
    -----------

    csv_date : datetime.date
        A date for which the CSV file has to opened (or downloaded and opened)
    
    company_name : str
        The accronym of the company for which the data is to be fetched 
    
    Returns:
    --------
     A list which contains the bhav_csv_data of the company for the provided date.

    """
    # TODO: Both date and company_name is mandatory. Check!

    print(f"read_single_csv: start: csv_date: [{csv_date}] company_name: [{company_name}] ")
    zip_file_name = nse_downloader.compose_file_path(csv_date).lstrip("/")
    print("read_single_csv: Zip File name: [ ", zip_file_name," ]")
    # Remove the trailing ".zip"
    tmp_file_name = zip_file_name.rstrip(".zip")
    csv_file_name = tmp_file_name + ".csv"
    print("read_single_csv: csv_file_name: [ ", csv_file_name," ]")
    # The bhav copies are in bhav_copy folder of current directory
    csv_file_path = os.path.join(nse_constants.BASE_DIR, csv_file_name)
    print("read_single_csv: CSV File path: [ ", csv_file_path," ]")
    if(not nse_downloader.check_file(csv_file_name)):
        print("read_single_csv: The required CSV file not found . . . Downloading!")
        url = nse_downloader.compose_url(csv_date)
        nse_downloader.download_file(url,os.path.join(os.path.curdir, "bhav_copy"))
    print("read_single_csv: File path for CSV: [ ", csv_file_path," ]")
    company_name_found = False
    
    list_of_dict = []
    with open(csv_file_path,'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            if line[0].upper() == company_name.upper():
                # print(line)
                company_name_found = True
                list_of_dict.append(make_stock_data_dict(line))
                # return line
            # else:
                # print("read_single_csv: File not found for ",csv_date)
                # print("read_single_csv: line[0]: [", line[0], "]")
                # pass
    # TODO if company name not found, return None and log
    if not company_name_found:
        print("read_single_csv: The data you are looking for is not found!")
        return None
    return list_of_dict

# Read data for a month
def read_monthly_csv(month_number = str,year_number = str,company_name = str):
    """Function to fetch bhav_csv_data of a company for a single month

    Parameters:
    -----------

    month_number : str
        The month reprsented in whole number

    year_number : str
        The year represented in whole number

    company_name : str
        The accronym of the company for which the data is to be fetched
    
    Returns:
    --------
     A list which contains the bhav_csv_data of the company for the provided month. 
    """
    stock_data_list = []
    # Verify if month_number input is valid
    flag = nse_downloader.check_month(month_number)
    flag = nse_downloader.check_year(year_number)
    if (flag == None):
        print("read_month_csv: Invalid month_number/year_number provided to the function")
        return None
    # monthly_list =[]  #Not needed because global stock_data_list is populated for every date
    for day_of_month in range(1,32):
        try:
            year_number = int(year_number)
            month_number = int(month_number)
            input_date = date(year_number,month_number,day_of_month)
            input_date = nse_downloader.verify_date(input_date)
            if (input_date == None):
              continue
            else:
                stock_data_list.append(read_daily_csv(input_date,company_name)) 
                # if ( daily_list != None):
                #     monthly_list.append(daily_list)
        except:
            continue        
    return stock_data_list

def read_yearly_csv(year_number = str, company_name = str):
    """Helper Function to fetch bhav_csv_data of a company for a single year

    Parameters:
    -----------
    year_number : str
        The year for which the csv_data is to be fetched, represented in whole numbers

    company_name : str
        The acrronym of the company listed in NSE for which the data is to be fetched.

    Returns:
    --------
    A list which contains the bhav_csv_data of the company for the provided year. 
    """
    year_number = nse_downloader.check_year(year_number)
    if (year_number == None):
        return None
    yearly_list = []
    for m in range(1,13):
        m = str(m)
        try:
            montly_list = read_monthly_csv(m,year_number,company_name)
            yearly_list.append(montly_list)
        except:
            continue
    return yearly_list    

def is_period_valid(period):
    """ Helper method to validate trading analysis period.
        Valid values for the period are Q1,Q2,Q3,Q4,H1,H2
        
    Parameters:
    -----------
    period: str

    Returns:
    --------
    True if the period is valid otherwise return False
    """
    valid_periods = nse_constants.valid_periods
    if(period):
        if(type(period) is str):
            # Check for valid type
            if (period.upper() in valid_periods):
                return True
            else:
                print("is_period_valid: Invalid value passed: ", period)
                return False
        else:
            print("is_period_valid: Invalid type passed for: ", period)
            return False
    print("is_period_valid: None value passed")
    return False

def process_input():
    print("Enter financial Period: ")
    period = input()
    period = period.upper()
    if (is_period_valid(period)):
        print("Enter the financial year")
        input_year = input()
        input_year = nse_downloader.check_year(input_year)
        if (input_year == None):
            return False
        if period == "Q1":
            for x in range(4,7):
                #read_monthly_csv has expected problems with date input check.
                x = str(x)
                read_monthly_csv(x,input_year)
        if period == "Q2":
            for x in range(7,10):
                #read_monthly_csv has expected problems with date input check.
                x = str(x)
                read_monthly_csv(x,input_year)
        if period == "Q3":
            for x in range(10,13):
                #read_monthly_csv has expected problems with date input check.
                x = str(x)
                read_monthly_csv(x,input_year)
        if period == "Q4":
            for x in range(1,4):
                #read_monthly_csv has expected problems with date input check.
                x = str(x)
                read_monthly_csv(x,input_year)
        if period == "H1":
            for x in range(4,10):
                #read_monthly_csv has expected problems with date input check.
                x = str(x)
                read_monthly_csv(x,input_year)
        if period == "H2":
            for x in range(10,13):
                #read_monthly_csv has expected problems with date input check.
                x = str(x)
                read_monthly_csv(x,input_year)
            for x in range(1,4):
                x = str(x)
                read_monthly_csv(x,input_year)    
    return None
    