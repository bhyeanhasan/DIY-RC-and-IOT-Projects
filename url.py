import requests

# url = "http://192.168.0.177:8000/api/customers/"
url = "www.google.com"

val = requests.get(url)

print(val)
