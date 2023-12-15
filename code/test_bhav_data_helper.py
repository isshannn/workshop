import unittest
import bhav_data_helper as nse_helper
import constants as nse_constants
from datetime import date

class test_data_csv(unittest.TestCase):
    def test_read_csv_for_company(self):
        valid_date = date(2023,10,27)
        valid_company_name = "INFY"
        result = nse_helper.read_csv_for_company(valid_date, valid_company_name)
        # result = result[0]
        # There are other ways to validate the o/p
        # but right now only company_name is checked in return
        print("test_read_daily_csv: result = ", result)
        self.assertEqual(result.get("SYMBOL"), valid_company_name)
        invalid_company_name = "SAMVAS"
        result = nse_helper.read_csv_for_company(valid_date, invalid_company_name)
        self.assertIsNone(result)
    
    def test_read_monthly_csv(self):
        valid_month = "7"
        valid_year = "2023"
        valid_company_name = "INFY"
        result = nse_helper.read_monthly_csv(valid_month,valid_year,valid_company_name)
        print(result)
        #Expect a list of dictionarioes in returns in return
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
        dummy_list = nse_helper.read_monthly_csv("10","2023","INFY")
        valid_key = "CLOSE"
        result = nse_helper.sort_list(dummy_list,valid_key)
        print("\n \n test_sort_list \n \n",result)

if __name__ == "__main__":
    unittest.main()