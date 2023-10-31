import unittest
import os
from file_download import file_downloader

class TestFileUtils(unittest.TestCase):
    def test_file_downloader(self):
        NSE_VALID_URL = "https://archives.nseindia.com/content/historical/EQUITIES/2023/OCT/cm27OCT2023bhav.csv.zip"
        self.assertIsNone(file_downloader(None))
        resp = file_downloader(NSE_VALID_URL)
        self.assertTrue(os.path.isfile("download.zip"))
if __name__ == "__main__":
    unittest.main()
