import os
from datetime import date
# contains all the holidays for last 5 years {2018-2023}
NSE_HOLIDAYS = [date(2022,8,9),date(2023,1,26),date(2023,3,7),date(2023,3,30),date(2023,4,4),date(2023,4,7),date(2023,4,14),date(2023,4,22),date(2023,5,1),date(2023,6,29),date(2023,8,15),date(2023,9,19),date(2023,10,2),date(2023,10,24),date(2023,11,14),date(2023,11,27),date(2023,12,25),date(2022,1,26),date(2022,3,1),date(2022,3,18),date(2022,4,14),date(2022,4,15),date(2022,5,3),date(2022,8,15),date(2022,8,31),date(2022,10,5),date(2022,10,24),date(2022,10,26),date(2022,10,26),date(2022,11,8),date(2021,1,26),date(2021,3,11),date(2021,3,29),date(2021,4,2),date(2021,4,14),date(2021,4,21),date(2021,5,13),date(2021,7,21),date(2021,8,19),date(2021,9,10),date(2021,10,15),date(2021,11,4),date(2021,11,5),date(2021,11,19),date(2020,2,21),date(2020,3,10),date(2020,4,2),date(2020,4,6),date(2020,4,10),date(2020,4,14),date(2020,5,1),date(2020,5,25),date(2020,10,2),date(2020,11,16),date(2020,11,30),date(2020,12,25),date(2019,1,26),date(2019,3,4),date(2019,3,21),date(2019,4,17),date(2019,4,19),date(2019,4,29),date(2019,5,1),date(2019,6,5),date(2019,8,12),date(2019,8,15),date(2019,9,2),date(2019,9,10),date(2019,10,2),date(2019,10,8),date(2019,10,21),date(2019,10,28),date(2019,11,12),date(2019,12,25),date(2018,1,26),date(2018,2,13),date(2018,3,2),date(2018,3,29),date(2018,3,30),date(2018,5,1),date(2018,5,22),date(2018,8,15),date(2018,9,13),date(2018,9,20),date(2018,10,2),date(2018,10,18),date(2018,11,7),date(2018,11,8),date(2018,11,23),date(2018,12,25)]
# base directory for downloaded bhav copies
BASE_DIR = os.path.join(os.getcwd(),'bhav_copy/')
BASE_URL = "https://archives.nseindia.com/content/historical/EQUITIES/"
valid_periods = ["Q1", "Q2", "Q3", "Q4","H1","H2"]
# https://wesmckinney.com/book/accessing-data#io_format_json

