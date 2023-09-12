import requests, json

# https://www.bigc.co.th/
#  delay 60 second

url = "https://openapi.bigc.co.th/customer/v1/otp"


headers = {
    'Authority': 'openapi.bigc.co.th',
    'Method': 'POST',
    'Path': '/customer/v1/otp',
    'Scheme': 'https',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'th-TH,th;q=0.9',
    'Content-Length': '25',
    'Content-Type': 'application/json',
    'Device-Info': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Language': 'th',
    'Origin': 'https://www.bigc.co.th',
    'Platform': 'web-desktop',
    'Referer': 'https://www.bigc.co.th/',
    'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': 'Windows',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Version': '1.13.10'
    
}

data = {"phone_no":"065000000000"}

res = requests.post(url, headers=headers, json=data).text

print(res)