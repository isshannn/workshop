import requests

def file_downloader(url):
    if (url):
        res = requests.get(url, allow_redirects=True)
        open("download.zip", 'wb').write(res.content)
    return None

