import webbrowser

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from setting import AmazonInfo

from core.cls.book import Book
from core.helper.const import DATA_DIR, END_TAG_FOR_INNER_JSON, PS_ADDED_TO_WL, START_TAG_FOR_INNER_JSON, WL_DIR


class Amazon:
    book_wishlist_share_link: str = AmazonInfo.book_wishlist_share_link

    wl_end_of_list_id = 'endOfListMarker'

    books_list_xpath = '//*[@id="g-items"]/li'
    book_main_xpath = "//div[starts-with(@id, 'itemMain')]"

    def __init__(self, browser: webdriver.Chrome):
        self.browser = browser

    def access_book_wl(self):
        self.browser.get(Amazon.book_wishlist_share_link)

    def scroll_to_last_of_wl(self):
        def is_last_of_wl():
            try:
                self.browser.find_element_by_id(Amazon.wl_end_of_list_id)
                return True
            except NoSuchElementException:
                return False

        html_elem = self.browser.find_element_by_tag_name('html')

        while not is_last_of_wl():
            html_elem.send_keys(Keys.PAGE_DOWN)

    def fetch_books_in_wl(self):
        books_id_elems = self.browser.find_elements_by_xpath(Amazon.book_main_xpath)
        books_a_elems = [book_elem.find_element_by_tag_name('h3').find_element_by_tag_name('a') for book_elem in
                         books_id_elems]
        assert len(books_id_elems) == len(books_a_elems)
        books_lis = [Book(amazon_link=book_a_elem.get_attribute('href'), amazon_book_title=book_a_elem.text,
                          amazon_book_id=book_id_elem.get_attribute('id')) for book_id_elem, book_a_elem in
                     zip(books_id_elems, books_a_elems)]
        return books_lis

    def save_page_html(self):
        with WL_DIR.joinpath('raw_wl.html').open('w') as f:
            html = self.browser.page_source
            f.write(html)


class MagicAmazon:
    start_tag_for_inner_json: str = START_TAG_FOR_INNER_JSON
    end_tag_for_inner_json: str = END_TAG_FOR_INNER_JSON
    postscript_to_wl: str = PS_ADDED_TO_WL

    def __init__(self):
        with WL_DIR.joinpath('raw_wl.html').open('r') as f:
            self.raw_wl = f.read()
        self.magic_wl = None

    def save_magic_wl_added_js(self):
        with WL_DIR.joinpath('magic_wl.html').open('w') as f_html:
            f_html.write(self.raw_wl)

            f_html.write(MagicAmazon.start_tag_for_inner_json)
            with DATA_DIR.joinpath('books.json').open('r') as f_json:
                books_json = f_json.read()
                f_html.write(books_json)
            f_html.write(MagicAmazon.end_tag_for_inner_json)

            f_html.write(MagicAmazon.postscript_to_wl)

    @staticmethod
    def open():
        webbrowser.open(str(WL_DIR.joinpath('magic_wl.html')))
