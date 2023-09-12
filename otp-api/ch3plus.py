import requests
#  https://ch3plus.com/
url = "https://api-sso.ch3plus.com/user/request-otp"

headers = {

    'authority':'api-sso.ch3plus.com',
    'method':'POST',
    'path':'/user/request-otp',
    'scheme':'https',
    'Accept':'application/json, text/plain, */*',
    'Accept-Encoding':'gzip, deflate, br',
    'Content-Type':'application/json',
    'Origin':'https://accounts.ch3plus.com',
    'Referer': 'https://accounts.ch3plus.com/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}



data = {"tel":"06000000000","type":"register"}

r = requests.post(url,headers=headers,json=data)

print(r.text)