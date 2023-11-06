import unittest
import os
import NSE_bhav_download as NSE
from datetime import date,datetime

class TestFileUtils(unittest.TestCase):
    def test_compose_url_for_year(self):
        test_year = "2022"
        # No need check for future year since compose_url_for_year inherits test_year
        test_year_null = None
        result = NSE.download_file_for_year(test_year)
        self.assertTrue(result)
        result = NSE.download_file_for_year(test_year_null)
        self.assertFalse(result)

    def test_compose_url_for_month(self):
        test_month = "2"
        test_year = "2023"
        test_month_invalid1 = "13"
        test_month_invalid2 = "0"
        test_month_invalid3 = "-22"
        test_month_null = None
        test_year_null = None
        result = NSE.download_file_for_month(test_month,test_year)
        self.assertTrue(result)
        result = NSE.download_file_for_month(test_month_invalid1,test_year)
        self.assertIsNone(result)
        result = NSE.download_file_for_month(test_month_invalid2,test_year)
        self.assertIsNone(result)
        result = NSE.download_file_for_month(test_month_invalid3,test_year)
        self.assertIsNone(result)
        result = NSE.download_file_for_month(test_month_null,test_year)
        self.assertIsNone(result)
        result = NSE.download_file_for_month(test_month_null,test_year)
        self.assertIsNone(result)
        result = NSE.download_file_for_month(test_month,test_year_null)
        self.assertIsNotNone(result)   


    def test_compose_url(self):
        test_date = date(2023,10,26)
        result = NSE.compose_url(test_date)
        expected_output = "https://archives.nseindia.com/content/historical/EQUITIES/2023/OCT/cm26OCT2023bhav.csv.zip"
        self.assertEqual(result, expected_output)

    def test_file_downloader(self):
        NSE_VALID_URL = "https://archives.nseindia.com/content/historical/EQUITIES/2023/OCT/cm27OCT2023bhav.csv.zip"
        self.assertIsNone(NSE.download_file(None,None))
        resp = NSE.download_file(NSE_VALID_URL,"cm27OCT2023bhav")
        self.assertTrue(os.path.isfile("bhav_copy/cm27OCT2023bhav.csv"))

    def test_verify_date(self):
        date_t_before = date(2023,2,23)
        date_t_after = date(2024,2,23)
        date_t_working_day = date(2023,11,3)
        date_t_holdiay = date(2023,1,26)
        date_Null= None
        date_weekday_Sun = date(2023,10,29)
        date_weekday_Sat = date(2023,10,28)
        #todays date
        result = NSE.verify_date(date_t_working_day)
        self.assertIsNotNone(result)
        #past date
        result = NSE.verify_date(date_t_before)
        self.assertIsNotNone(result)
        #future date
        result = NSE.verify_date(date_t_after)
        self.assertIsNone(result)
        #NULL Input
        result = NSE.verify_date(date_Null)
        self.assertIsNone(result)
        #Holiday date input
        result = NSE.verify_date(date_t_holdiay)
        self.assertIsNone(result)
        #Weekday date input
        result1 = NSE.verify_date(date_weekday_Sat)
        result2 = NSE.verify_date(date_weekday_Sun)
        self.assertIsNone(result1)
        self.assertIsNone(result2)

    
    def test_month(self):
        month_range = "4"
        month_out_range = "15"
        month_string = "abc"
        month_Null = None
        #Valid Input between 1 to 12
        result = NSE.check_month(month_range)
        self.assertIs(type(result),int)
        #Invalid Input for number > 12
        result = NSE.check_month(month_out_range)
        self.assertIsNone(result)
        #Invald Input String
        result =  NSE.check_month(month_string)
        self.assertIsNone(result)
        #None/NULL Input
        result = NSE.check_month(month_Null)
        self.assertIsNone(result)

    def test_day(self):
        day_valid = "18"
        day_invalid1 = "38"
        day_invalid2 = "0"
        day_invalid3 = "-21"
        day_invalid4 = "4.1"
        day_string = "abc"
        day_Null= None
        #Valid Input
        result = NSE.check_day(day_valid)
        self.assertIs(type(result),int)
        #Invalid Input for >31
        result = NSE.check_day(day_invalid1)
        self.assertIsNone(result)
        #Invalid Input for <1
        result1 = NSE.check_day(day_invalid2)
        result2 = NSE.check_day(day_invalid3)
        self.assertIsNone(result1)
        self.assertIsNone(result2)
        #Invalid Input Floating
        result = NSE.check_day(day_invalid4)
        self.assertIsNone(result)
        #Invalid Input String
        result = NSE.check_day(day_string)
        self.assertIsNone(result)
        #Null Input
        result = NSE.check_day(day_Null)
        self.assertIsNone(result)
    
    def test_year(self):
        y_valid = "2001"
        y_invalid = date.today()
        # To fetch current year and add 1 to it so as it becomes invalid
        y_invalid = y_invalid.strftime("%Y") 
        y_invalid = int(y_invalid)
        y_invalid = y_invalid + 1
        y_invalid = str(y_invalid)
        y_string = "abc"
        #Valid Input
        result = NSE.check_year(y_valid)
        self.assertIsNotNone(result)
        #Invalid Input
        result = NSE.check_year(y_invalid)
        self.assertIsNone(result)
        #Check for string
        result= NSE.check_year(y_string)
        self.assertIsNone(result)

        def test_file(self):
            result = NSE.file_check("cm27OCT2023bhav.csv")
            self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()