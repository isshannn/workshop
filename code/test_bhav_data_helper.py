import unittest
import bhav_data_helper as nse_helper
import constants as nse_constants
from datetime import date, timedelta
from pandas import DataFrame as df

class test_data_csv(unittest.TestCase):
    def test_read_csv_for_company(self):
        valid_date = date(2023,10,27)

        # Test for valid company name
        valid_company_name = "INFY"
        result = nse_helper.read_csv_for_company(valid_date, valid_company_name)
        # result = result[0]
        # There are other ways to validate the o/p
        # but right now only company_name is checked in return
        print("test_read_daily_csv: result = ", result)
        self.assertEqual(result.get("SYMBOL"), valid_company_name)
        
        # Test for invalid company
        invalid_company_name = "SAMVAS"
        result = nse_helper.read_csv_for_company(valid_date, invalid_company_name)
        self.assertIsNone(result)
    
    def test_return_single_day_csv(self):
        # Check for normal input
        input_1 = date(2021,2,23)
        result = nse_helper.return_single_day_csv(input_1)
        self.assertIsInstance(result,df)

        # check for holiday input
        input_2 = date(2021,8,15)
        result = nse_helper.return_single_day_csv(input_2)
        self.assertIsNone(result)
    
    def test_read_monthly_csv(self):
        valid_month = "7"
        valid_year = "2023"
        valid_company_name = "INFY"
        invalid_year = date.today()
        invalid_year = invalid_year + timedelta(days=365)
        invalid_year = invalid_year.strftime("%Y")

        # Test for invalid year
        print("test_read_montly_csv :: invalid_year = ",invalid_year)
        result = nse_helper.read_monthly_csv_for_company(valid_month,invalid_year,valid_company_name)

        #Test for Valid company_name expect a list of dictionarioes in returns in return
        result = nse_helper.read_monthly_csv_for_company(valid_month,valid_year,valid_company_name)
        print(result)
        self.assertIsInstance(result,list)

    def test_yearly_csv_for_company(self):
        valid_company_name = "INFY"

        # Check for invalid year
        input_invalid_year = date.today() + timedelta(days=365)
        input_invalid_year = input_invalid_year.strftime("%Y")
        result = nse_helper.read_yearly_csv_for_company(input_invalid_year,valid_company_name)
        self.assertIsNone(result)  
        
        # Check for valid input 
        input_valid_year = str(int(input_invalid_year) - 1)
        result = nse_helper.read_yearly_csv_for_company(input_valid_year,valid_company_name)
        self.assertIsInstance(result,list)

    # def test_feed_list(self):
    #     list_1 = ['INFY', 'EQ', '1363.65', '1385', '1363.65', '1380.35', '1381.05', '1359.45', '4634358', '6395268362.3', '27-OCT-2023', '160477', 'INE009A01021', '']
    #     list_2 = ['DUMB_INFY', 'EQ', '1363.65', '1385', '1363.65', '1380.35', '1381.05', '1359.45', '4634358', '6395268362.3', '27-OCT-2023', '160477', 'INE009A01021', '']          
    #     # nse_helper.feed_stock_data_list(list_1)
    #     # nse_helper.feed_stock_data_list(list_2)
    #     self.assertIsInstance(nse_helper.stock_data_list,list)
    
    def test_is_period_valid(self):
        result = nse_helper.is_period_valid(None)
        # when None is passed expect False value returned
        self.assertFalse(result)
        # When a valid string value is passed, expect True
        for x in nse_constants.valid_periods:
            result = nse_helper.is_period_valid(x)
            self.assertTrue(result)
        # When int (or any non-string) is passed, expect False
        result = nse_helper.is_period_valid(100)
        self.assertFalse(result)
        # when invalid value for str is passed, expect False
        result = nse_helper.is_period_valid("mon")
        self.assertFalse(result)
    
    # def test_process_input(self):
    #     result = nse_helper.process_input()
    #     self.assertIsNone(result)

    def test_sort_list(self):
        dummy_list = nse_helper.read_monthly_csv_for_company("10","2023","INFY")
        valid_key = "CLOSE"
        print("\n \n test_sort_list :: input\n \n",dummy_list)
        print("\n \n test_sort_list :: valid_key\n \n",valid_key)
        
        result = nse_helper.sort_list(dummy_list,valid_key)
        print("\n \n test_sort_list :: result \n \n",result)

if __name__ == "__main__":
    unittest.main()
