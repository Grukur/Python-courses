from Clase_11.Milestone_Scrape.locators.quotes_locators import QuoteLocators


class QuoteParser:
    """
    Given one of the specific quote divs, find out the
    data out the quote (quote content, author tags).
    """

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Quote {self.content}, by {self.author}'

    @property
    def content(self):
        locator = QuoteLocators.CONTENT
        return self.parent.select_one(locator).string.replace('£', "") # se modifico y agrego .replace()

    @property
    def author(self):
        locator = QuoteLocators.AUTHOR
        return self.parent.select_one(locator).attrs['title'] # se modifico y agrego .attrs[]

    @property
    def tags(self):
        locator = QuoteLocators.TAGS
        item_rate = self.parent.select_one(locator)
        classes = item_rate.attrs['class']

        cla = [p for p in classes if 'star-rating' != p]  # se cambio completamente
        return cla[0]



