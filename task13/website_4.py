import requests

url = 'https://www.google.com/'
try:
    res = requests.get(url)
except requests.exceptions.RequestException:
    print("Error connecting to the website")
else:
    content = res.text
    print("O",content)
