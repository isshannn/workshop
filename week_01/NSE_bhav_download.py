import requests
from zipfile import ZipFile
from datetime import date
import os
from constants import BASE_DIR, NSE_HOLIDAYS, BASE_URL

def check_day(argument):
    if(argument):
        if(argument.isdecimal()):
            d = int(argument)
            if( d>0 and d<32):
                return d
            else:
                return None
        return None
    return None

def check_month(argument):
    if(argument):
        if(argument.isdecimal()):
            m = int(argument)
            if(m>0 and m < 13):
                return m;
            else:
                return None
        return None
    return None   

def check_year(argument):
    if(argument):
        if(argument.isdecimal()):
            y = int(argument)
            td = date.today()
            td = td.strftime("%Y")
            td = int(td)
            if (y > td):
                return None
            return y
        return None
    return None    

def file_downloader(url):
    if (url):
        print("URL to download: [", url, "]")
        res = requests.get(url, allow_redirects=True)
        f = open("download.zip", 'wb').write(res.content)
        # f = open(os.path.join(BASE_DIR,"download.zip"), 'wb').write(res.content)
        # Make sure to change to the addresses below correctly for smooth running
        # the adresses here point to the zip file downloaded and to where it's extracted
        print(BASE_DIR)
        print("AAA [", os.path.join(BASE_DIR,"download.zip"), "]")
        with ZipFile(os.path.join(BASE_DIR,"download.zip"), "r") as unzip:
            unzip.extractall(path=BASE_DIR)
        if (os.path.exists(os.path.join(BASE_DIR,"download.zip"))):
            os.remove(os.path.join(BASE_DIR,"download.zip"))
    return None

def verify_date(argument):
    if(argument):
        t_date =  date.today()
        if (t_date < argument):
            return None
        if (t_date == argument):
            return None
        if(t_date > argument):
            return argument

print("Enter Date")
# dd = input()
dd = "26"
dd = check_day(dd)

print("Enter Month")
# mm = input()
mm = "10"
mm = check_month(mm)

print("Enter Year")
yy = "2023"
# yy = input()
yy = check_year(yy)

#stores the date input by the user
input_date = date(yy,mm,dd)
input_date = verify_date(input_date)



# tempstr to write date as str format in the url
file_url = BASE_URL + input_date.strftime("%Y") + "/" + input_date.strftime("%b").upper() + "/cm" + input_date.strftime("%d") + input_date.strftime("%b").upper() + input_date.strftime("%Y") +"bhav.csv.zip"
print(file_url)

file_downloader(file_url)