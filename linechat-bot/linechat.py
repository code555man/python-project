import requests
 
url = 'https://notify-api.line.me/api/notify'

token = "YOUR_TOKEN"

headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
 
msg = 'Demo Send Message'

r = requests.post(url, headers=headers , data = {'message':msg})

print(r.text)