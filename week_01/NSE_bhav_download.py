import requests
from datetime import date

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
        res = requests.get(url, allow_redirects=True)
        f = open("download.zip", 'wb').write(res.content)
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

# print("Enter Date")
# dd = input()
# dd = check_day(dd)

# print("Enter Month")
# mm = input()
# mm = check_month(mm)

# print("Enter Year")
# yy = input()
# yy = check_year(yy)



