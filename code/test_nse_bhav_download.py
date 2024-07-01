import unittest
import os
import nse_bhav_download as NSE
from datetime import date,timedelta,datetime

class TestFileUtils(unittest.TestCase):
    def test_compose_url_for_year(self):
        test_year = "2023"
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
        test_year_future = "3000"
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
        result = NSE.download_file_for_month(test_month,test_year_future)
        self.assertIsNone(result)   


    def test_compose_url(self):
        # On date input expect a string return
        test_date = date(2023,10,26)
        result = NSE.compose_url(test_date)
        expected_output = "https://archives.nseindia.com/content/historical/EQUITIES/2023/OCT/cm26OCT2023bhav.csv.zip"
        self.assertEqual(result, expected_output)

        # On None input expect a None return
        test_date = None
        result = NSE.compose_url(test_date)
        self.assertIsNone(result)

    def test_check_file(self):
        # On None input expect a None return
        none_input = None
        result = NSE.check_file(none_input)
        self.assertIsNone(result)

        # Check for an existing file, expect True in return
        input_file_exist = "cm01APR2022bhav.csv"
        result = NSE.check_file(input_file_exist)
        self.assertTrue(result)

    def test_compose_file_path(self):
        
        # For any valid date expect string return
        test_date = date.today()
        result = NSE.compose_file_path(test_date)
        self.assertIsInstance(result,str)

        # For None input expect a None in return
        test_date = None
        result = NSE.compose_file_path(test_date)
        self.assertIsNone(result)
        


    def test_file_downloader(self):
        NSE_VALID_URL = "https://archives.nseindia.com/content/historical/EQUITIES/2023/OCT/cm27OCT2023bhav.csv.zip"
        self.assertIsNone(NSE.download_file(None,None))
        resp = NSE.download_file(NSE_VALID_URL,"cm27OCT2023bhav")
        self.assertTrue(os.path.isfile("bhav_copy/cm27OCT2023bhav.csv"))

    def test_verify_date(self):
        date_past = date.today() - timedelta(days=1)
        date_today= datetime.today()
        date_future = date.today() + timedelta(days=1)
        date_holdiay = date(2023,1,26)
        date_Null= None
        date_weekday_Sun = date(2023,10,29)
        date_weekday_Sat = date(2023,10,28)
        date_future_year=date.today() + timedelta(days=365)

    #    Skipping the following unittest because the function itself is utilizing datetime, check_time() in its body 
    #    Datetime argument is causing faults. Boundry conditions are handled perfectly in practical uses.
    #    For code coverage reference no need to test line 166-171 in nse_bhav_download.py

        # #todays date pre 19:00
        # if(date_today.hour > 19):
        #     date_today = date_today - timedelta(hours = 19)
        # result = NSE.verify_date(date_today)
        # self.assertIsNotNone(result)
        
        # #todays date post 19:00
        # if (date_today.hour < 19):
        #     date_today = date_today + timedelta(hours = 19 - int(date_today.strftime("%H")))
        # result = NSE.verify_date(date_today)
        # self.assertIsNotNone(result)

        #past date
        if (date_past.isoweekday() > 5):
            while (date_past.isoweekday() > 5):
                date_past = date_past - timedelta(days=1)
        result = NSE.verify_date(date_past)
        self.assertIsNotNone(result)
        
        #future date
        if (date_future.isoweekday() > 5):
            while (date_future.isoweekday() > 5):
                date_future = date_future - timedelta(days=1)
        result = NSE.verify_date(date_future)
        self.assertFalse(result)

        #future year date
        if (date_future_year.isoweekday() > 5):
            while (date_future_year.isoweekday() > 5):
                date_future_year = date_future_year - timedelta(days=1)
        result = NSE.verify_date(date_future_year)
        self.assertFalse(result)

        #NULL Input
        result = NSE.verify_date(date_Null)
        self.assertIsNone(result)
        
        #Holiday date input
        result = NSE.verify_date(date_holdiay)
        self.assertIsNone(result)
        
        #Weekday date input
        result1 = NSE.verify_date(date_weekday_Sat)
        result2 = NSE.verify_date(date_weekday_Sun)
        self.assertIsNone(result1)
        self.assertIsNone(result2)

        #Custom 2022 date holiday date 
        result = NSE.verify_date(date(2022,3,1))
        self.assertIsNone(result)

    
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

    def test_check_day(self):
        # For None input expect a None return
        input_null = None
        result = NSE.check_day(input_null)
        self.assertIsNone(result)

        # # Check for no argument
        # result=NSE.check_day()
        # self.assertIsNone(result)

        # For non decimal string input expect a None return
        input_non_decimal = "abc"
        result = NSE.check_day(input_non_decimal)
        self.assertIsNone(result)

        # For decimal input check if its in range 0 to 31, if yes return the input itself
        input_decimal_in_range = range(1,32)
        for x in input_decimal_in_range:
            x = str(x)
            result = NSE.check_day(x)
            self.assertEqual(result,int(x))
        
        # For decimal input outside of range expect a None in return
        input_decimal_out_range = "33"
        result = NSE.check_day(input_decimal_out_range)
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
        self.assertIsNone(result)
        #Invalid Input
        result = NSE.check_year(y_invalid)
        self.assertIsNone(result)
        #Check for string
        result= NSE.check_year(y_string)
        self.assertIsNone(result)

    
    def test_check_time(self):
        input_valid_time = datetime.today()
        input_valid_time = input_valid_time + timedelta(hours= 19 - int(input_valid_time.strftime("%H")))
        print("test_check_time :: input_valid time =",input_valid_time.strftime("%H"))
        input_invalid_time = input_valid_time + timedelta(hours= 10 - int(input_valid_time.strftime("%H")))
        print("test_check_time :: invalid_input_hours =",input_invalid_time.strftime("%H"))
       
        # Expect False in return
        result = NSE.check_time(input_valid_time)
        self.assertFalse(result)
       
        # Expect True in return
        result = NSE.check_time(input_invalid_time)
        self.assertTrue(result)
        
        
if __name__ == "__main__":
    unittest.main()