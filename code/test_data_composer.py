import unittest
import data_composer 
import pandas as pd
import json
from datetime import date,timedelta

# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)
# # pd.set_option('display.max_colwidth', -1)

td_1 = timedelta(days=1)

# For validating json output
def validate_json_syntax(d):
    try:
        json.loads(d)
        return True
    except ValueError:
        print('validate_json_syntax :: JSON data contains an error :  \n',ValueError)
        return False

class test_weekly_data_csv(unittest.TestCase):
    def test_nearest_trading_day(self):
        
        # check for past Saturday Input (16/12/2023) Expect it to return 11/12/2023
        input_Sat_date = date(2023,12,16)
        print("test_nearest_trading_day :: input_Sat_date = ",input_Sat_date,input_Sat_date.strftime("%a"))
        result = data_composer.nearest_trading_day(input_Sat_date)
        print("test_nearest_trading_day :: Function Output = ",result,result.strftime("%a"))
        self.assertEqual(result,date(2023,12,11))

        # check for coming(future) Sunday Input Expect it to return False
        input_Sun_date = date.today() + timedelta(days=(7 - date.today().isoweekday()))
        print("test_nearest_trading_day :: input_Sun_date = ",input_Sun_date, input_Sun_date.strftime("%a"))
        result = data_composer.nearest_trading_day(input_Sun_date)
        print("test_nearest_trading_day :: Function Output = ",result)
        self.assertEqual(result,False)

        # check for past date input, on a random weekday
        input_random_date = date(2023,3,24)
        print("test_nearest_trading_day :: input_random_date = ",input_random_date,input_random_date.strftime("%a"))
        result = data_composer.nearest_trading_day(input_random_date)
        print("test_nearest_trading_day :: Function Output = ",result,result.strftime("%a"))
        self.assertEqual(result.isoweekday(),1)

        # check for future date, Expect a False return
        input_future_date = date.today() + timedelta(days=2)
        print("test_nearest_trading_day :: input_future_date = ",input_future_date,input_future_date.strftime("%a"))
        result = data_composer.nearest_trading_day(input_future_date)
        print("test_nearest_trading_day :: Function Output = ",result)
        self.assertEqual(result,False)

        # Check for Holiday date
        input_holiday_date=date(2023,1,26)
        print("test_nearest_trading_day :: input_holiday_date = ",input_holiday_date,input_future_date.strftime("%a"))
        result = data_composer.nearest_trading_day(input_holiday_date)
        print("test_nearest_trading_day :: Function Output = ",result)
        self.assertIsInstance(result,date)

    
    def test_compose_weekly_csv(self):
       
        # Test for last week files, Expect a pandas.Dataframe object in return
        input_last_monday_date = date.today() - (7*td_1)
        while(input_last_monday_date.isoweekday() != 1):
            input_last_monday_date = input_last_monday_date - td_1
        print("test_compose_weekly_csv :: input_last_monday_date= ",input_last_monday_date,input_last_monday_date.strftime("%a"))
        result = data_composer.compose_weekly_csv(input_last_monday_date)
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
        result = data_composer.compose_weekly_csv(input_ongoing_monday_date)
        print("test_compose_weekly_csv :: Function Output \n ")
        print(result)
        self.assertIsNone(result)

        # Test for future date. Except a None in return
        input_future_date = date.today() + timedelta(days=11)
        print("test_compose_weekly_csv :: input_future_date= ",input_future_date,input_ongoing_monday_date.strftime("%a"))
        result = data_composer.compose_weekly_csv(input_future_date)
        print("test_compose_weekly_csv :: Function Output \n ")
        print(result)
        self.assertIsNone(result)

    def test_compose_monthly_data(self):
        input_month_number_valid = 11
        input_year_number_valid = 2023
        input_month_number_invalid = -2
        input_month_number_invalid2 = 13
        input_year_number_invalid = 2000
        input_year_number_invalid2 = date.today()
        input_year_number_invalid2 = int(input_year_number_invalid2.strftime("%Y"))
        input_year_number_invalid2 = input_year_number_invalid2 + 1

        # Check for valid month and valid year input, expect a pandas.dataframe() object in return
        print("test_compose_montly_data :: Function input = ", input_month_number_valid, " ", input_year_number_valid)
        result = data_composer.compose_monthly_file(input_month_number_valid,input_year_number_valid)
        print("test_compose_montly_data :: Output = ", result)
        self.assertIsInstance(result,pd.DataFrame)

        # Check for invalid month and valid year input, expect a None return
        print("test_compose_montly_data :: Function input = ", input_month_number_invalid, " ", input_year_number_valid)
        result = data_composer.compose_monthly_file(input_month_number_invalid,input_year_number_valid)
        print("test_compose_montly_data :: Output = ", result)
        self.assertIsNone(result)

        print("test_compose_montly_data :: Function input = ", input_month_number_invalid2, " ", input_year_number_valid)
        result = data_composer.compose_monthly_file(input_month_number_invalid2,input_year_number_valid)
        print("test_compose_montly_data :: Output = ", result)
        self.assertIsNone(result)

        # Check for valid month and invalid year input, expect a None return
        print("test_compose_montly_data :: Function input = ", input_month_number_valid, " ", input_year_number_invalid)
        result = data_composer.compose_monthly_file(input_month_number_valid,input_year_number_invalid)
        print("test_compose_montly_data :: Output = ", result)
        self.assertIsNone(result)

        print("test_compose_montly_data :: Function input = ", input_month_number_valid, " ", input_year_number_invalid2)
        result = data_composer.compose_monthly_file(input_month_number_valid,input_year_number_invalid2)
        print("test_compose_montly_data :: Output = ", result)
        self.assertIsNone(result)

        
   
    def test_compose_company_file(self):

        # If correct arguments are passed,Expect a DataFrame object in return
        input_company_name = "INFY"
        input_file = data_composer.compose_weekly_csv(data_composer.nearest_trading_day(date(2023,12,13)))
        print("test_compose_company_file :: input_company_name = ",input_company_name)
        result = data_composer.compose_company_file(input_file,input_company_name)
        print("test_compose_company_file :: Function Output = ")
        print(result)
        self.assertIsInstance(result,pd.DataFrame)

        # On None inputs expect None in return
        input_none_file = None
        input_none_company = None
       
        print("test_compose_company_file :: input_none_file = ",input_none_file)
        result = data_composer.compose_company_file(input_none_file,input_company_name)
        print("test_compose_company_file :: Function Output = ")
        print(result)
        self.assertIsNone(result)
      
        print("test_compose_company_file :: input_none_company = ",input_none_company)
        result = data_composer.compose_company_file(input_file,input_none_company)
        print("test_compose_company_file :: Function Output = ")
        print(result)
        self.assertIsNone(result)

        


    def test_bhav_to_csv(self):
        input_file = data_composer.compose_weekly_csv(data_composer.nearest_trading_day(date(2023,12,13)))
        print("test_bhav_to_csv :: Function Input \n",input_file)
        data_composer.bhav_to_csv(input_file)
    
    def test_view_gain_loss_weekly(self):
        # Test for current date expect some error
        input_date = date.today()
        print("test_view_gain_loss_weekly :: input : ", input_date)
        result = data_composer.view_Gain_loss_all_weekly(input_date)
        print("test_view_gain_loss_weekly :: result : \n", result)

        # Test for future expect none in return
        input_future_date=date.today() + timedelta(days=1)
        print("test_view_gain_loss_weekly :: input : ", input_future_date)
        result = data_composer.view_Gain_loss_all_weekly(input_future_date)
        print("test_view_gain_loss_weekly :: result : \n", result)
        self.assertIsNone(result)

        # Test for past date, expect a json object in return
        print("test_view_gain_loss_weekly :: input : ", date(2023,2,23))
        result = data_composer.view_Gain_loss_all_weekly(date(2023,2,23))
        result = validate_json_syntax(result)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()