__author__ = 'Tarrok'

import requests
from bs4 import BeautifulSoup as bs

request = requests.get('https://www.johnlewis.com/house-by-john-lewis-hinton-office-chair/black/p4201464')
content = request.content
soup = bs(content, 'html.parser')
element = soup.find(name='div', class_='prices-container').p.text.strip()
print(element)

clean_price = float(element[1:])
print(f'{clean_price:.2f}')
