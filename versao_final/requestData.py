import requests
from lxml import html

# Requests data from a website, parsing its information as well
def requestPageData(url):
	try:
		r = requests.get(url)
	except requests.exceptions.Timeout:
	    print("Connection with vultr.com timed out, verify your connection or retry later.")
	except requests.exceptions.TooManyRedirects:
	    print("Connection had too many redirects, double-check your url.")
	except requests.exceptions.RequestException as e:
		print(e)
		exit()
	return html.fromstring(r.content)