import requests
#  https://register.sabuyebuy.com/otp-required
url = "https://www.sabuyebuy.com/wp-json/api/v3/send-x"

headers = {
    'authority':'www.sabuyebuy.com',
    'method':'POST',
    'path':'/wp-json/api/v3/send-x',
    'scheme':'https',
    'Accept':'application/json, text/plain, */*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'th;q=0.6',
    'Content-Type':'application/json',
    'Origin':'https://register.sabuyebuy.com',
    'Referer':'https://register.sabuyebuy.com/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

data = {"id":"ea2saQ==","phone":"06000000"}

r = requests.post(url,headers=headers,json=data)

print(r.text)