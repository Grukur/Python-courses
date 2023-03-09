from bs4 import BeautifulSoup

from Clase_11.Milestone_Scrape.locators.quotes_pages_locators import QuotesPageLocators
from Clase_11.Milestone_Scrape.parsers.quotes import QuoteParser


class QuotePage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def quotes(self):
        locator = QuotesPageLocators.QUOTE
        quote_tags = self.soup.select(locator)
        return [QuoteParser(e) for e in quote_tags]
