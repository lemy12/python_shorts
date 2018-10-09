import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.nytimes.com/')
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')
title = soup.find_all("span",{"class":"ghost"})

print (title)