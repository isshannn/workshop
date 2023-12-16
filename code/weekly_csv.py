from datetime import date, timedelta
import pandas as pd
import nse_bhav_download as nse_date_checker
import bhav_data_helper as nse_csv_composer
import constants

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
    
    """
    td_1 = timedelta(days=1)
    weekday_status = start_date.isoweekday()
    file = pd.DataFrame()
    while(weekday_status < 6):
        file = file._append(nse_csv_composer.return_entire_csv(start_date), ignore_index = True)
        print(start_date.strftime("%a"))
        start_date = start_date + td_1
        weekday_status = start_date.isoweekday()
    return file