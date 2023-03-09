import requests
from bs4 import BeautifulSoup
import openpyxl

url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
content = soup.find_all('tbody', class_='lister-list')
movies = []

for item in content:
    for x in item:
        try:
            deep = x.find('td', class_='titleColumn').a.text
            rating = x.find('td', class_='ratingColumn imdbRating').strong.text
            movies.append((deep, rating))
        except:
            continue

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'Movies'
sheet['A1'] = 'Year'
sheet['B1'] = 'Movie'

for movie in movies:
    sheet.append(movie)

wb.save('movies-2019.xlsx')