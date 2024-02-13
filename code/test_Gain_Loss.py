import unittest
import data_composer 
import pandas as pd
from datetime import date,timedelta

class test_weekly_data_csv(unittest.TestCase):
    def test_Gain_loss(self):
        data_composer.view_Gain_loss_all_weekly(date(2024,1,2))
if __name__ == '__main__':
    unittest.main()
