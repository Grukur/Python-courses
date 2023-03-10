from typing import List
from selenium.webdriver.support.ui import Select

from Clase_12.Quotes_page_locator_selenium import QuotesPageLocators
from Clase_12.Quotes_quotes_selenium import QuoteParser


class QuotesPage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def quotes(self) -> List[QuoteParser]:
        return [QuoteParser(e) for e in self.browser.find_elements_by_css_selector(QuotesPageLocators.QUOTE)]

    @property
    def author_dropdown(self) -> Select:
        element = self.browser.find_element_by_css_selector(QuotesPageLocators.AUTHOR_DROPDOWN)
        return Select(element)

    @property
    def tags_dropdown(self) -> Select:
        element = self.browser.find_element_by_css_selector(QuotesPageLocators.TAG_DROPDOWN)
        return Select(element)

    @property
    def search_button(self):
        return self.browser.find_element_by_css_selector(QuotesPageLocators.SEARCH_BUTTON)


    def select_author(self, author_name: str):
        self.author_dropdown.select_by_visible_text(author_name)


    def get_available_tags(self) -> List[str]:
        return [option.text.strip() for option in self.tags_dropdown.options]
    
    def select_tag(self, tag_name: str):
        self.tags_dropdown.select_by_visible_text(tag_name)
