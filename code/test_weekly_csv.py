import unittest
import weekly_csv 
import pandas as pd
from datetime import date,timedelta

# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)
# # pd.set_option('display.max_colwidth', -1)

td_1 = timedelta(days=1)

class test_weekly_data_csv(unittest.TestCase):
    def test_nearest_trading_day(self):
        
        # check for past Saturday Input (16/12/2023) Expect it to return 11/12/2023
        input_Sat_date = date(2023,12,16)
        print("test_nearest_trading_day :: input_Sat_date = ",input_Sat_date,input_Sat_date.strftime("%a"))
        result = weekly_csv.nearest_trading_day(input_Sat_date)
        print("test_nearest_trading_day :: Function Output = ",result,result.strftime("%a"))
        self.assertEqual(result,date(2023,12,11))

        # check for coming(future) Sunday Input Expect it to return False
        input_Sun_date = date.today() + timedelta(days=(7 - date.today().isoweekday()))
        print("test_nearest_trading_day :: input_Sun_date = ",input_Sun_date, input_Sun_date.strftime("%a"))
        result = weekly_csv.nearest_trading_day(input_Sun_date)
        print("test_nearest_trading_day :: Function Output = ",result)
        self.assertEqual(result,False)

        # check for past date input, on a random weekday
        input_random_date = date(2023,3,24)
        print("test_nearest_trading_day :: input_random_date = ",input_random_date,input_random_date.strftime("%a"))
        result = weekly_csv.nearest_trading_day(input_random_date)
        print("test_nearest_trading_day :: Function Output = ",result,result.strftime("%a"))
        self.assertEqual(result.isoweekday(),1)

        # check for future date, Expect a False return
        input_future_date = date.today() + timedelta(days=2)
        print("test_nearest_trading_day :: input_future_date = ",input_future_date,input_future_date.strftime("%a"))
        result = weekly_csv.nearest_trading_day(input_future_date)
        print("test_nearest_trading_day :: Function Output = ",result)
        self.assertEqual(result,False)

    
    def test_compose_weekly_csv(self):
        # Test for last week files, Expect a pandas.Dataframe object in return
        input_last_monday_date = date.today() - (7*td_1)
        while(input_last_monday_date.isoweekday() != 1):
            input_last_monday_date = input_last_monday_date - td_1
        print("test_compose_weekly_csv :: input_last_monday_date= ",input_last_monday_date,input_last_monday_date.strftime("%a"))
        result = weekly_csv.compose_weekly_csv(input_last_monday_date)
        print("test_compose_weekly_csv :: Function Output \n ")
        print(result)
        self.assertIsInstance(result,pd.DataFrame)

        # Test for ongoing Monday input, Expect None in return
        input_ongoing_monday_date = date.today()
        if(input_ongoing_monday_date.isoweekday() == 7):
            input_ongoing_monday_date = input_ongoing_monday_date + td_1
        else: 
            while(input_ongoing_monday_date.isoweekday() != 1):
                input_ongoing_monday_date = input_ongoing_monday_date - td_1
        print("test_compose_weekly_csv :: input_ongoing_monday_date= ",input_ongoing_monday_date,input_ongoing_monday_date.strftime("%a"))
        result = weekly_csv.compose_weekly_csv(input_ongoing_monday_date)
        print("test_compose_weekly_csv :: Function Output \n ")
        print(result)
        self.assertIsNone(result)
   
    def test_compose_company_file(self):
        # Expect a DataFrame object in return
        input_company_name = "INFY"
        input_file = weekly_csv.compose_weekly_csv(weekly_csv.nearest_trading_day(date(2023,12,13)))
        print("test_compose_company_file :: input_company_name = ",input_company_name)
        result = weekly_csv.compose_company_file(input_file,input_company_name)
        print("test_compose_company_file :: Function Output = ")
        print(result)
        self.assertIsInstance(result,pd.DataFrame)

    def test_bhav_to_csv(self):
        input_file = weekly_csv.compose_weekly_csv(weekly_csv.nearest_trading_day(date(2023,12,13)))
        print("test_bhav_to_csv :: Function Input \n",input_file)
        weekly_csv.bhav_to_csv(input_file)
    

if __name__ == '__main__':
    unittest.main()