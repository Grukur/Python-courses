from selenium import webdriver

from Clase_12.Quotes_pages_selenium import QuotesPage


chrome = webdriver.Chrome(executable_path="E:\Python Trash\ChromeDriver\chromedriver.exe")
chrome.get("http://quotes.toscrape.com/search.aspx")
page = QuotesPage(chrome)


author = input("Enter the author you'd like quote from: ")
page.select_author(author)

tags = page.get_available_tags()
print("Select one of these tags: [{}]".format(' | '.join(tags)))
selected_tag = input("Enter your tag: ")

page.select_tag(selected_tag)
page.search_button.click()

print(page.quotes)


