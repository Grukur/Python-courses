from Clase_13.Book_Scraper_async.app import books
import logging

USER_CHOICE = '''Enter one of the following
- 'b' to look at 5-star books
- 'c' to look at the cheapest books
- 'n' to just get the next available book on the page
- 'q' to exit
Enter your choice: '''

logger = logging.getLogger('scraping.Menu')


def print_best_book():
    logger.info('Finding best book by rating and price...')
    best_books = sorted(books, key=lambda x: (x.rating * -1, x.price))[:10]
    for book in best_books:
        print(book)


def print_cheapest_book():
    logger.info('Finding cheapest book...')
    cheap_books = sorted(books, key=lambda x: x.price)[:10]
    for book in cheap_books:
        print(book)


gen = (x for x in books)


def get_next_book():
    logger.info('Finding next book...')
    print(next(gen))

############## nueva forma de definir un menu, on diccionario #############

user_choices = {
    'b': print_best_book,
    'c': print_cheapest_book,
    'n': get_next_book
}


def menu():
    user = input(USER_CHOICE)
    while user != 'q':
        if user in ('b', 'c','n'):
            user_choices[user]()
        else:
            print('error')
        user = input(USER_CHOICE)
    print('Good day, you leave this site')
    logger.debug('Ending App')

menu()





