import requests

def fetchandsave(url, path):
    r = requests.get(url)
    with open(path, 'w') as f:
        f.write(r.text)

url = "https://timesofindia.indiatimes.com"

fetchandsave(url, "data/times.html")
open("data/times.html", "r").read()