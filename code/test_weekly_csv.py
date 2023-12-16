import unittest
import weekly_csv as wk
import pandas as pd
from datetime import date,timedelta

class test_weekly_data_csv(unittest.TestCase):
    def test_nearest_trading_day(self):
        
        # check for current Saturday Input (16/12/2023) Expect it to return 11/12/2023
        input_Sat_date = date(2023,12,16)
        print("test_nearest_trading_day :: input_Sat_date = ",input_Sat_date)
        result = wk.nearest_trading_day(input_Sat_date)
        print("test_nearest_trading_day :: Function Output = ",result,result.strftime("%a"))
        self.assertEqual(result,date(2023,12,11))

        # check for coming Sunday Input (17/12/2023) Expect it to return False
        input_Sun_date = date(2023,12,17)
        print("test_nearest_trading_day :: input_Sun_date = ",input_Sun_date)
        result = wk.nearest_trading_day(input_Sun_date)
        print("test_nearest_trading_day :: Function Output = ",result)
        self.assertEqual(result,False)

        # check for past date input, on a random weekday
        input_random_date = date(2023,3,24)
        print("test_nearest_trading_day :: input_random_date = ",input_random_date,input_random_date.strftime("%a"))
        result = wk.nearest_trading_day(input_random_date)
        print("test_nearest_trading_day :: Function Output = ",result,result.strftime("%a"))
        self.assertEqual(result.isoweekday(),1)

        # check for future date, Expect a False return
        input_future_date = date.today() + timedelta(days=2)
        print("test_nearest_trading_day :: input_future_date = ",input_future_date,input_future_date.strftime("%a"))
        result = wk.nearest_trading_day(input_future_date)
        print("test_nearest_trading_day :: Function Output = ",result)
        self.assertEqual(result,False)
    
    def test_compose_weekly_csv(self):

        # Compose file for previous week wrt dt. 16/12/2023(Sat)
        input_date = date(2023,12,4)
        result = wk.compose_weekly_csv(input_date)
        print(result)
        self.assertIs(type(result),pd.DataFrame)

        # Compose file for current week wrt dt 16/12/2023(Sat)
        result = wk.compose_weekly_csv(date(2023,12,11))
        print(result)
        self.assertIs(type(result),pd.DataFrame)

if __name__ == '__main__':
    unittest.main()