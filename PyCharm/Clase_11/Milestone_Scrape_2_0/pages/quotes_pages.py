import re
import logging


from bs4 import BeautifulSoup
from Clase_11.Milestone_Scrape_2_0.locators.quotes_pages_locators import AllBooksPageLocators
from Clase_11.Milestone_Scrape_2_0.parsers.quotes import BookParser


logger = logging.getLogger('scarping.quotes_pages')


class AllBooksPage:
    def __init__(self, page):
        logger.debug('Parsing page content with BeautifulSoup HTML parser.')
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        logger.debug(f'Finding all books in the page using `{AllBooksPageLocators.BOOKS}`')
        return [BookParser(e) for e in self.soup.select(AllBooksPageLocators.BOOKS)]

    @property
    def page_count(self):
        logger.debug('Finding all number of catalogue pages...')
        content = self.soup.select_one(AllBooksPageLocators.PAGE).string
        logger.info(f'found number of catalogue pages available: `{content}`.')
        pattern = 'Page [0-9]+ of ([0-9]+)'
        matcher = re.search(pattern, content)
        pages = int(matcher.group(1))
        logger.debug(f'Extracted number of pages as integer: `{pages}`.')
        return pages



