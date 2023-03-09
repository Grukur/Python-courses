import requests
import logging

from Clase_11.Milestone_Scrape_2_0.pages.quotes_pages import AllBooksPage

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', # da formato a como se muestran los logs
    datefmt='%d-%m-%Y %H:%M:%S', # format time in log
    level=logging.INFO, # define el grado de alerta minimo a mostrar
    filename='logs_scraping.txt' # indica el archivo donde guardara los logs
)

logger = logging.getLogger('scraping')

logger.info('Loading books list...')

page_content = requests.get('http://books.toscrape.com').content
page = AllBooksPage(page_content)

books = []

for page_num in range(page.page_count):
    url = f'http://books.toscrape.com/catalogue/page-{page_num+1}.html'
    page_content = requests.get(url).content
    logger.debug('Creating book list')
    page = AllBooksPage(page_content)
    books.extend(page.books) # extend concatena listas y append agrega elementos a una lista



#for quote in books.quotes:
#    print('price is', quote.content, 'for the book', quote.author, 'and with a rating of', quote.tags, 'stars', 'you can find in: ', quote.link)