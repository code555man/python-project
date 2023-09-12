import  requests

# delay 3 minuted
#  https://www.lotuss.com/th/register

url = "https://shoponline-bffapi.lotuss.com/bff/customer/v1/customers/registration/send-otp"

headers = {
    
    'Authority': 'shoponline-bffapi.lotuss.com',
    'Method': 'POST',
    'Path': '/bff/customer/v1/customers/registration/send-otp',
    'Scheme': 'https',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'th',
    'Authorization': 'eyJraWQiOiJPMGRLVm1VcGx1a29ZVk9oMHd5S00wZ2ZHMEVJTnJkSit3T290VFdlKzlVPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIxNnRkaHBydjlkb2phb3Q3NTZtYXY2bDBjOSIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoic2VydmljZS1hcGlcL2dlbmVyYWwiLCJhdXRoX3RpbWUiOjE2ODkxMzQ1MTUsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5hcC1zb3V0aGVhc3QtMS5hbWF6b25hd3MuY29tXC9hcC1zb3V0aGVhc3QtMV8waVZXa2JHTjYiLCJleHAiOjE2ODkxMzgxMTUsImlhdCI6MTY4OTEzNDUxNSwidmVyc2lvbiI6MiwianRpIjoiM2E3MDIzZGMtODE4MC00Njc1LWI1NGItMTFmZWJkZTZiMjY4IiwiY2xpZW50X2lkIjoiMTZ0ZGhwcnY5ZG9qYW90NzU2bWF2NmwwYzkifQ.PuS2foTMjdvKi4ORvWZwhxv1NPKIBTVNYrzv55IjQKdPJ8pwOwAuitSkgUgNoAwgmeljZe3HuuwSLtxIyNbW5q-6eC6FGOvDrZDS_AIHU3Ah5WGhs1Kla8bbQ-wnyOSShbmFlDkfld2eHkflFIf_VchP_Xf6Zvp3l55L3YqQhwC9jFM6g9mPovuh50JjGFWB7VcozXloZcUiS0s14Aj5gBgH890eUEqlrlUT4O58lM6_0oN6ZkyWH2s3y37m73TOcvV5TX_kXghcbGRVG4YJVgYHmnmeKFGq0nIMtXj6PhhqXIJRvi1_7V94B83EMFGOU-4pwqtoFQ9XuS9ZtnWLXA',
    'Content-Length': '212',
    'Content-Type': 'application/json',
    'Origin': 'https://www.lotuss.com',
    'Referer': 'https://www.lotuss.com/',
    'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': 'Windows',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'X-Correlation-Id': 'e0811722-cef6-4625-b356-a0202c631b91'

}

data = {"messageTemplate":"รหัส OTP โค้ดของคุณคือ {OTP} รหัสมีอายุชั่วคราวอยู่ 3 นาที (Ref. {RefCode})","mobileNumber":"66650000000000"}

res = requests.post(url, headers=headers, json=data).text
print("Done",res)
