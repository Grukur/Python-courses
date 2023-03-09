import re
import logging

from Clase_11.Milestone_Scrape_2_0.locators.quotes_locators import BookLocators

logger = logging.getLogger('scraping.quotes')

class BookParser:
    """
    Given one of the specific quote divs, find out the
    data out the quote (quote content, author tags).
    """
    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5,
    }

    def __init__(self, parent):
        logger.debug(f'New book parser created from `{parent}`.')
        self.parent = parent

    def __repr__(self):
        return f'{self.name} at ${self.price} with a rate of {self.rating} Stars, in website {self.link}'

    @property
    def price(self):
        logger.debug('Getting Book Price...')
        locator = BookLocators.PRICE_LOCATOR
        return self.parent.select_one(locator).string.replace('£', "") # se modifico y agrego .replace()

    @property
    def name(self):
        logger.debug('Getting Book Name...')
        locator = BookLocators.NAME_LOCATOR
        return self.parent.select_one(locator).attrs['title'] # se modifico y agrego .attrs[]

    @property
    def rating(self):
        logger.debug('Getting Book Rating...')
        locator = BookLocators.RATING_LOCATOR
        item_rate = self.parent.select_one(locator)
        classes = item_rate.attrs['class']
        cla = [p for p in classes if 'star-rating' != p]  # se cambio completamente
        return BookParser.RATINGS.get(cla[0], 'No Rate')

    @property
    def link(self):
        logger.debug('Getting Book Link...')
        locator = BookLocators.LINK_LOCATOR
        return self.parent.select_one(locator).attrs['href']










