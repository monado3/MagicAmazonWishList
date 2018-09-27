from selenium import webdriver

from core.cls.amazon import Amazon, MagicAmazon
from core.cls.book import Books


def fetch_from_Amazon(wl_name: str, wl_link: str) -> Books:
    browser = webdriver.Chrome()
    amazon = Amazon(browser, wl_name, wl_link)
    amazon.access_book_wl()
    amazon.scroll_to_last_of_wl()
    book_lis = amazon.fetch_books_in_wl()
    amazon.save_page_html()
    browser.close()

    books = Books(wl_name, book_lis)
    books.check_book_is_cached()
    books.get_info_from_cache()
    books.fetch_ISBNs()
    return books


def gen_books_from_cache(wl_name: str) -> Books:
    books = Books(wl_name, None)
    books.books_in_latest_wl = books.books_in_cached_wl
    return books


def fetch_from_OPAC_and_save(books: Books, mode: str):
    books.fetch_opac_links(mode)
    books.fetch_reg_nums_in_opac(mode)
    books.save_books_as_json()


def make_and_open_wishlist(wl_name):
    magic_amazon = MagicAmazon(wl_name)
    magic_amazon.save_magic_wl_added_js()
    magic_amazon.open()
