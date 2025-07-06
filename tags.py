import requests
from bs4 import BeautifulSoup

with open("sample.html", "r") as f:
    html_doc = f.read()

soup =. BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())
 
for links in soup.find_all('a'):
    print(links.get('href'))

