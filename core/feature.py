from selenium import webdriver

from core.cls.amazon import Amazon, MagicAmazon
from core.cls.book import Books


def fetch_from_Amazon():
    browser = webdriver.Chrome()
    amazon = Amazon(browser)
    amazon.access_book_wl()
    amazon.scroll_to_last_of_wl()
    book_lis = amazon.fetch_books_in_wl()
    amazon.save_page_html()
    browser.close()

    books = Books()
    books.books_in_latest_wl = book_lis
    books.check_book_is_cached()
    books.get_info_from_cache()
    books.fetch_ISBNs()
    return books


def gen_books_from_cache():
    books = Books()
    books.books_in_latest_wl = books.books_in_cached_wl
    return books


def fetch_from_OPAC_and_save(books: Books, mode: str):
    books.fetch_opac_links(mode)
    books.fetch_reg_nums_in_opac(mode)
    books.save_books_as_json()


def make_and_open_wishlist():
    magic_amazon = MagicAmazon()
    magic_amazon.save_magic_wl_added_js()
    magic_amazon.open()
