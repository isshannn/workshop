import csv
import nse_bhav_download as file_handler

#OBJECTIVES: FETCH FILES FOR A MONTH

#Check file integrity 
##1> Check if the file for the current date is present
##2> If not then download it
##3> Get the file name for the date

#Read a company data for a given period
def read_company_data(company_name, period = None):
    return None
#Obtain the data for a single day

def read_csv_day(args_date):
    """Opens csv file for a single day

    Parameters:
    -----------

    args_date :  datetime.date
        Is the date for which the csv file is to be created and or searched for and data is fecthed for it

    Returns:
    --------
    An dictionary containing all the symbols for a given date. 
    None if the date is invalid.
    """
    # You need to check here if the file is present or not before operating.
    file_path = file_handler.compose_file_path(args_date)
    if(file_path == None):
        return None
    else:
        file_url = file_handler.compose_url(args_date)
        file_handler.download_file(args_date,file_path)
    with open(file_path,'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            print(csv_file[1])

#Obtain the data for a month
def read_csv_month(args_month_number):
    """Opens a csv file for a single month
    """
    pass