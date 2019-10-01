import requests
url = 'http://localhost:5000/'
r = requests.post(url,json={'params':[0, 20, 20]})
print(r.json())