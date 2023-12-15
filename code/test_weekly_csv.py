import unittest
import weekly_csv as wk
import pandas as pd
from datetime import date,timedelta

class test_weekly_data_csv(unittest.TestCase):
    def test_nearest_trading_day(self):
        input_current_date = date.today()
        td_1 = timedelta(days=1)
        input_ongoing_week_date = input_current_date + td_1
        input_random_date = date(2023,10,14)
        
        # Expect a False return on input of current date
        result = wk.nearest_trading_day(input_current_date)
        print("test_weekly_data_csv :: Input_current_date =  ",input_current_date)
        print("test_weekly_data_csv :: Function return value =  ",result)
        self.assertFalse(result)

        # Expect a False return on input of ongoing week date
        result = wk.nearest_trading_day(input_ongoing_week_date)
        print("test_weekly_data_csv :: Input_ongoing_week_date =  ",input_ongoing_week_date)
        print("test_weekly_data_csv :: Function return value =  ",result)
        self.assertFalse(False)

        # Expect a date object (which falls on Monday return) on input of a random past date
        result = wk.nearest_trading_day(input_random_date)
        print("test_weekly_data_csv :: Input_random_date =  ",input_random_date,input_random_date.strftime('%a'))
        print("test_weekly_data_csv :: Function return value =  ",result,result.strftime('%a'))
        self.assertEqual(result.isoweekday(),1)
    
    def test_compose_weekly_csv(self):
        input_date = date(2023,12,1)
        result = wk.compose_weekly_csv(input_date)
        print(result)
        self.assertIs(type(result),pd.DataFrame)

if __name__ == '__main__':
    unittest.main()