from selenium import webdriver

from core.cls.amazon import Amazon, MagicAmazon
from core.cls.book import Books


def main():
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
    books.fetch_opac_links()
    books.fetch_reg_nums_in_opac()
    books.save_books_as_json()

    magic_amazon = MagicAmazon()
    magic_amazon.save_magic_wl_added_js()
    magic_amazon.open()


if __name__ == '__main__':
    main()
