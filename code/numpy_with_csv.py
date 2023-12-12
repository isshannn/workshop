import bhav_data_helper as bhav_helper
import numpy as np
from datetime import date

# Fetch a list of dictionaries
data_oct_2023_infy = bhav_helper.read_monthly_csv("12","2023","INFY")
# data_oct_2023_infy = np.array(data_oct_2023_infy)
# print(data_oct_2023_infy)
for x in data_oct_2023_infy:#[0].keys():
    print(x)

key_numpy_array = np.array([])
    
"""
data_oct_2023_infy is a numpy array which contains dictioneries in ascending order of working days. Now how to play around by fetching data from
each dictionary?

there is a function in bhav_data_helper which sorts data accroding to the key provided, probably in ascending order.
"""

