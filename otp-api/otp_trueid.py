import requests

# delay in web 60 second or set to delay 20
#  https://tv.trueid.net/live/mono29

url = "https://identity.trueid.net/api/otp/request"

headers = {
    'Authority':'identity.trueid.net',
    'Method':'POST',
    'Path':'/api/otp/request',
    'Scheme':'https',
    'Accept':'application/json',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'th-TH,th;q=0.9',
    'Access-Control-Allow-Origin':'*',
    'Client_timezone':'Asia/Bangkok',
    'Content-Length':'126',
    'Content-Type':'application/json; charset=UTF-8',
    'Cookie':'visid_incap_2624018=Y1fczEOcR4e4l7dh0dlOAIrkimQAAAAAQUIPAAAAAAD/VUNmrSuheCU5SAiSE8mz; incap_ses_219_2624018=LL3QFQZNu0EjAduz1AsKA4rkimQAAAAAj3em8tJnB8RTmzJ8gOoEjg==; visid_incap_2104120=CjXp8oteR2C8Tni+B2ayp4vkimQAAAAAQUIPAAAAAABFN+4IvV+O83O2ZqByiOOk; incap_ses_960_2104120=7uCAaxCsHR0ylHfL0ptSDYvkimQAAAAAprLR9KKe+/stzQY6FPZGow==; _csrf=snP3_UzmPQP7n2faKqxpf5Pe; visid_incap_2679318=2TVxyUaeSaG4sag1UN0CyozkimQAAAAAQUIPAAAAAAA6BQii5s/hLqqNNdAz6ivI; nlbi_2679318=Ta5QSy0dNSP9EQe9YwCYNQAAAABa/+h3Dno0KdNqIL6dkFy1; incap_ses_219_2679318=XybDL0xNGVLIBduz1AsKA4zkimQAAAAABpBaoH2mkyDEgaWQeCiDGA==; sessioncenter=s%3ASgdFxenUkyjg9UKdvP9qYXd6de39kfL4.gEuzjrg6sbSX06co2uW5RHPVAWJ067uKg7Tg7ElaD0U; nol_fpid=mweq4ec2bmvjjpigvcslbzfqjmjhl1686824076|1686824076491|1686824076491|1686824076491; _gid=GA1.2.127212053.1686824077; unique_user_id=454657852.1686824076; _gcl_au=1.1.1838576107.1686824077; __gads=ID=a714631fa595e5b5:T=1686824078:RT=1686824078:S=ALNI_May-NVr_8XwoJwvaww3w0UMR_F_gA; __gpi=UID=00000c13af614374:T=1686824078:RT=1686824078:S=ALNI_MbaryJJTFkwiFO37_4sYWtObFwFTg; _cbclose=1; _cbclose26068=1; _uid26068=D377FACB.1; _ctout26068=1; OptanonConsent=isIABGlobal=false&datestamp=Thu+Jun+15+2023+17%3A14%3A37+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.13.0&hosts=&landingPath=https%3A%2F%2Ftv.trueid.net%2Flive%2Fmono29&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0005%3A1; _fbp=fb.1.1686824077601.1596539977; _tt_enable_cookie=1; _ttp=l3ydo8jiVl2fLbR96oQ8ii6cG8K; panoramaId_expiry=1686910481023; _cc_id=202d975463d02a5fcb1dc5cb00dfe116; panoramaId=79b281f31223c95388e5481b4c25a9fb927a5617784b07eeabfcb395ee85cb31; cto_bundle=vPlkzl9kc0xZV05VTVQlMkZuenFLTm1EaUQ4c3dGbTVSR1B1QzVid3RjZkJpMGcwWEt0UlRoMnU4T2QxbEhjcWdzOGwlMkI3Wnp2dXJrN3RCeGQ3SlpZaDRDUG5vZThOdTl2S1dzbEViS0JUM2MzSDZ6V0o4cU9xVHh5RVMwbEl1TDFneEZKZE9kNSUyRk92M1VOdHNOQUNGNGh4UiUyQnRwZyUzRCUzRA; cto_bidid=qwDhvF8lMkYxSHlpSDdMbjRERHlWMmFKTG9JdHdKQVRKQ3E2Q053czNKTGdwRldlWiUyRnBxc2ZSbFhvQVFEOGFzOU5TOHBMV3BvUHBWT3hLSjhQTnh5QmpRY0thbWgycktHOHFjZkw3Z1RsQ1NKYXl4eTAlM0Q; _ga_id=454657852.1686824076; afUserId=29e0d096-54d7-4621-acb2-3bc01b5099ca-p; AF_SYNC=1686824079512; verify=test; __lt__cid=d70a95eb-2162-40eb-875f-655ddd3da352; __lt__sid=ec1635fc-68bf83d5; _ga=GA1.2.454657852.1686824076; csrf_token_aaa=XAzo2j3l-AoFgT75xllmBXpphYl1xmwRyM-8; _ga_R05PJC3ZG8=GS1.1.1686824077.1.1.1686824118.19.0.0',
    'Newrelic':'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjEyNzkyMTIiLCJhcCI6IjE3MjE5Njg4NzEiLCJpZCI6IjMwZWY1MDBkNDViMjAwZjgiLCJ0ciI6ImE5NmZiYzI2NzRiODA3OTg4OWZkZjc2MGVmMDUyYjcwIiwidGkiOjE2ODY4MjQxNTUyNzV9fQ==',
    'Origin':'https://identity.trueid.net',
    'Referer':'https://identity.trueid.net/verify?client_id=931&redirect_uri=https%3A%2F%2Ftv.trueid.net&flow=popup&lang=th&scope=public_profile%2Cmobile%2Cemail%2Creferences%2Cidentity_account_read%2Cidentity_token_bridge&state=1&browser_id=126446.1702877580',
    'Sec-Ch-Ua':'"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'Sec-Ch-Ua-Mobile':'?0',
    'Sec-Ch-Ua-Platform':'Windows',
    'Sec-Fetch-Dest':'empty',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Site':'same-origin',
    'Traceparent':'00-a96fbc2674b8079889fdf760ef052b70-30ef500d45b200f8-01',
    'Tracestate':'1279212@nr=0-1-1279212-1721968871-30ef500d45b200f8----1686824155275',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'X-Csrf-Token':'XAzo2j3l-AoFgT75xllmBXpphYl1xmwRyM-8'
}


data = {"client_id":"931","lang":"th","type":"mobile","account":"06500000000","country_code":"66","device_id":"web_126446.1702877580"}

res = requests.post(url,headers=headers,json=data).text

print(res)