import requests
import time
import aiohttp
import asyncio

from Clase_13.Book_Scraper_async.pages.quotes_pages import AllBooksPage

loop = asyncio.get_event_loop()

page_content = requests.get('http://books.toscrape.com').content
page = AllBooksPage(page_content)

books = []

async def fetch_page(session, url):
    page_start = time.time()
    async with session.get(url) as response:
        print(f'page took: {time.time() - page_start}')
        return await response.text()


async def get_multi_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks


urls = [f'http://books.toscrape.com/catalogue/page-{page_num+1}.html' for page_num in range(1, page.page_count)]
start = time.time()
pages = loop.run_until_complete(get_multi_pages(loop, *urls))
print(f'All took: {time.time() - start}')

for page_content in pages:
    page = AllBooksPage(page_content)
    books.extend(page.books)

print(books)





