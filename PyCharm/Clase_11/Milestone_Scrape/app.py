import requests

from Clase_11.Milestone_Scrape.pages.quotes_pages import QuotePage

page_content = requests.get('http://books.toscrape.com/').content
page = QuotePage(page_content)

for quote in page.quotes:
    print('price is', quote.price, 'for the book', quote.name, 'and with a rating of', quote.tags, 'stars')