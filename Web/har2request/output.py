import requests

url = "http://www.example.com/"
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "de,en-US;q=0.7,en;q=0.3",
    "Connection": "keep-alive",
    "Host": "www.example.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0"
}
post_data = {}
r = requests.get(url,headers=headers, data=post_data)

url = "http://www.example.com/favicon.ico"
headers = {
    "Accept": "image/avif,image/webp,*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "de,en-US;q=0.7,en;q=0.3",
    "Connection": "keep-alive",
    "Host": "www.example.com",
    "Referer": "http://www.example.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0"
}
post_data = {}
r = requests.get(url,headers=headers, data=post_data)

