from Clase_12.Quotes_locators_selenium import QuoteLocators


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
        return self.parent.find_element_by_css_selector(locator).text

    @property
    def author(self):
        locator = QuoteLocators.AUTHOR
        return self.parent.find_element_by_css_selector(locator).text

    @property
    def tags(self):
        locator = QuoteLocators.TAGS
        return self.parent.find_elements_by_css_selector(locator)


