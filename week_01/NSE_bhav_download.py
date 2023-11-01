import requests
from datetime import date

def file_downloader(url):
    if (url):
        res = requests.get(url, allow_redirects=True)
        f = open("download.zip", 'wb').write(res.content)
    return None

def verify_date(argument):
    if(argument):
        t_date =  date.today()
        return t_date

# print("Enter Date")
# dd = input()

