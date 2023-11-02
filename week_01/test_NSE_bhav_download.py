import unittest
import os
import NSE_bhav_download as NSE
from datetime import date

class TestFileUtils(unittest.TestCase):
    def test_file_downloader(self):
        NSE_VALID_URL = "https://archives.nseindia.com/content/historical/EQUITIES/2023/OCT/cm27OCT2023bhav.csv.zip"
        self.assertIsNone(NSE.file_downloader(None))
        resp = NSE.file_downloader(NSE_VALID_URL)
        self.assertTrue(os.path.isfile("download.zip"))

    def test_date(self):
        date_t_before = date(2023,2,23)
        date_t_after = date(2024,2,23)
        date_t_today = date.today()
        date_t_holdiay = date(2023,1,26)
        date_Null= None
        date_weekday_Sun = date(2023,10,29)
        date_weekday_Sat = date(2023,10,28)
        #todays date
        result = NSE.verify_date(date_t_today)
        self.assertIsNone(result)
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

if __name__ == "__main__":
    unittest.main()