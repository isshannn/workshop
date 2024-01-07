from datetime import date, timedelta
import pandas as pd
import numpy as np
import nse_bhav_download as nse_date_checker
import bhav_data_helper as nse_csv_composer
import os

def nearest_trading_day(input_date : date):
    """Function returns the date which falls on Monday of the input date's week. If the input_date is of an incomplete on going week, returns False.
    Parameters:
    -----------
    input_date : date
        A date which is scanned to be a weekday or weekend.
    
    Returns:
    --------
    output_date : date
        Nearest trading date which falls on Monday, wrt to input_date.
    False if the Input date is in future/on-going week
    """
    current_date = date.today()
    date_status = nse_date_checker.verify_date(input_date)
    td_1 = timedelta(days=1)

    # Considering Week is from (Sun-Sat) if the input is ongoing Sat,i.e the last day of week returns Monday of the same on-going week
    if(input_date.isoweekday() == 6 and input_date == current_date):
        return (input_date - (5*td_1))
    if(input_date.isoweekday() == 7 and input_date >= current_date):
        print("nearest_trading_day :: CANT FETCH FILES FOR THE UPCOMING WEEK. PLEASE ENTER A PAST DATE")
        return False
    # print("nearest_trading_day :: date_status =  ",date_status)
    if (date_status == None or type(date_status) == date):
        week_of_day = input_date.isoweekday()
        while(week_of_day != 1):
            input_date = input_date - td_1
            week_of_day = input_date.isoweekday()
        return input_date
    if (not type(date_status) == False):
        print("nearest_trading_day :: CANT FETCH FILES FOR THE UPCOMING WEEK. PLEASE ENTER A PAST DATE")
        return False

def compose_weekly_csv(start_date : date):
    """This function returns a group of csv files for the working days of the week wrt the start date, which must be a MONDAY
    Parameters:
    -----------
    start_date : date
        Is a date which falls on Monday.
    Returns:
    --------
    file : pandas.DataFrame
        A pandas.DataFrame object which contains merged contents of each bhav_copy of the day in the duration of a week.

    None
        If start date falls on an incomplete week (A week is considered to be from Mon-Fri)    
    """
    start_date = nearest_trading_day(start_date)
    td_1 = timedelta(days=1)
    weekday_status = start_date.isoweekday()
    if(start_date + (5*td_1) >= date.today()):
        print("compose_weekly_csv :: CANT FETCH DATA FOR ONGOING WEEK")
        return None
    file = pd.DataFrame()
    temp_date = start_date
    while(weekday_status < 6):
        temp_date = nse_date_checker.verify_date(temp_date)
        if (temp_date != None):
                file = file._append(nse_csv_composer.return_entire_csv(temp_date), ignore_index = True)
                temp_date = temp_date + td_1
                start_date = start_date + td_1
                weekday_status = temp_date.isoweekday()
        else:
            temp_date = start_date
            temp_date = temp_date + td_1

    del file["Unnamed: 13"]
    counter = 0
    for value in file["SERIES"]:
        if(value != "EQ"):
            # pass
            # Push the entire row here.
            # sorted_file = sorted_file._append(file.iloc[counter], ignore_index = True)
            file = file.drop(counter)
        counter = counter + 1
    # playground_file(file)
    return file

def compose_company_file(file : pd.DataFrame, company_name: str):
    """Helper function which constructs a DataFrame for storing a Company's weekly bhav_data
    Parameters:
    -----------
    file : pandas.DataFrame
        A Dataframe which contains bhav_data of all listed companies for a duration of an entire week

    company_name : str
        A str object representing the SYMBOL of the listed company in bhav_data

    Returns:
    --------
    company_file : pandas.DataFrame
        A DataFrame which contains the bhav_data of the input company for the duration of a week    
    """
    if(type(file) == None):
        print("compose_company_file :: File not found")
        return None
    company_file = file.loc[file.SYMBOL == company_name]
    # This is to suppress warning about SettingWithCopyWarning
    # For more information and bug fixes go to: 
    # https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
    with pd.option_context('mode.chained_assignment',None):
        company_file["GAIN_LOSS"] = ( ( company_file["CLOSE"] - company_file["OPEN"] ) / company_file["OPEN"] ) * 100
    return company_file


def bhav_to_csv(file : pd.DataFrame):
    """Helper function which creates csv_file which stores merged daily bhav_data, of each individual listed company, in the duration of a single week.
    
    Parameters:
    -----------
    file : pandas.DataFrame
        A DataFrame which contains daily bhav_data of each listed company, in a duration of one week
    
    Returns:
    ---------
    None
        This Function creates X.csv files [X being the SYMBOL of the comapny listed] in the folder company_bhav_copy inside the bhav_copy folder, make sure to create a folder beforehand in order for smooth functiong of code
    
    """
    # Stores each listed company symbol in a series
    companies = file.SYMBOL.unique()
    for x in companies:
        data_frame = compose_company_file(file,x)
        csv_file_name = x + ".csv"
        try:
            data_frame.to_csv(path_or_buf=os.path.join(os.getcwd(),'bhav_copy/company_bhav_copy/')+csv_file_name, mode='w')
        except Exception as E:
            print("bhav_to_csv :: the following Error occured during creation: ", E)
            continue
    return None
    
def view_Gain_loss_all_weekly(start_date : date):
    """A function which returns a DataFrame containing SYMBOL(unique),FirstOPEN,LastClose,Gain_Loss for the entire week
    
    Parameters:
    -----------
        start_date: datetime.date
            The input with respect to which end user want to fetch weekly bhav_data
    
    Returns:
    --------
        Gain_Loss_Data_Frame.to_json() 
            A json file containing weekly bhav_data
        
        False 
            If file is not composed for the current week.

    """
    start_date = nearest_trading_day(start_date)
    if(type(start_date) != date):
        print("INVALID INPUT")
        return None
    file = compose_weekly_csv(start_date)
    if (file == None):
        return False
    bhav_to_csv(file)
    Gain_Loss_Data_Frame = pd.DataFrame(columns = ["SYMBOL","FIRST_OPEN","LAST_CLOSE","GAIN_LOSS"])
    Gain_Loss_Data_Frame["SYMBOL"] = file.SYMBOL.unique()
    First_Open_list = []
    Last_Close_list = []
    for x in Gain_Loss_Data_Frame.SYMBOL:
        company_file = pd.read_csv(os.path.join(os.getcwd(),'bhav_copy/company_bhav_copy/')+x+".csv")
        company_file_length = company_file.SYMBOL.count() - 1
        First_Open_list.append(company_file.loc[0].OPEN)
        Last_Close_list.append(company_file.loc[company_file_length].CLOSE)
    Gain_Loss_Data_Frame["FIRST_OPEN"] = First_Open_list
    Gain_Loss_Data_Frame["LAST_CLOSE"] = Last_Close_list
    Gain_Loss_Data_Frame["GAIN_LOSS"] = ( (Gain_Loss_Data_Frame["LAST_CLOSE"] - Gain_Loss_Data_Frame["FIRST_OPEN"]) / Gain_Loss_Data_Frame["FIRST_OPEN"] ) * 100
    print(Gain_Loss_Data_Frame)
    return Gain_Loss_Data_Frame.to_json()
