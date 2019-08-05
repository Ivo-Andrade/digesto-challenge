from datetime import datetime    
import requests
import urllib.request
import json
import faster_than_request as rq

print(datetime.now())
url = "https://www.vultr.com/products/cloud-compute/"

req = requests.Session()
req.trust_env = False
req = requests.get(url, headers={'Connection': 'close'}, stream=True)

req = urllib.request.urlopen(url)

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read()

req = rq.gets(url)

print("R")
print(datetime.now())

print(req.encoding)
print(datetime.now())