import unittest
import os
import NSE_bhav_download as NSE
from datetime import date

class TestFileUtils(unittest.TestCase):
    # def test_file_downloader(self):
    #     NSE_VALID_URL = "https://archives.nseindia.com/content/historical/EQUITIES/2023/OCT/cm27OCT2023bhav.csv.zip"
    #     self.assertIsNone(file_downloader(None))
    #     resp = file_downloader(NSE_VALID_URL)
    #     self.assertTrue(os.path.isfile("download.zip"))

    def test_date(self):
        date_t_before = date(2023,2,23)
        date_t_after = date(2024,2,23)
        date_t_today = date.today()
        #todays date
        result = NSE.verify_date(date_t_today)
        self.assertIsNone(result)
        #past date
        result = NSE.verify_date(date_t_before)
        self.assertIsNotNone(result)
        #future date
        result = NSE.verify_date(date_t_after)
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()