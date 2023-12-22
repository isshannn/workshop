import unittest
import weekly_csv 
import pandas as pd
from datetime import date,timedelta

class test_weekly_data_csv(unittest.TestCase):
    def test_Gain_loss(self):
        weekly_csv.view_Gain_loss_all_weekly()
if __name__ == '__main__':
    unittest.main()