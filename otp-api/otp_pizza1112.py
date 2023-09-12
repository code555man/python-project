import requests,time

# delay 60 second 

url = "https://api2.1112.com/api/v1/otp/create"

headers = {
    'Authority': 'api2.1112.com',
    'Method': 'POST',
    'Path': '/api/v1/otp/create',
    'Scheme': 'https',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'th-TH,th;q=0.9',
    'Content-Length': '44',
    'Content-Type' : 'application/json;charset=UTF-8',
    'Origin' : 'https://1112.com',
    'Referer': 'https://1112.com/',
    'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': "Windows",
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

data = {"phonenumber":"065000000000","language":"th"}

for i in range(10):

    res  = requests.post(url, headers=headers, json=data).text
    print(res)
    time.sleep(60)  
# print(res)