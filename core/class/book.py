import json
from collections import defaultdict
from threading import Thread

from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

from core.classes.opac import OPAC
from core.helper.const import DATA_DIR
from core.helper.function import exists_cache, requests_get_as_fox

options = Options()
options.set_headless(True)


class Book:
    def __init__(self, **kwargs):
        default_kwargs = defaultdict(lambda: None, kwargs)

        self.amazon_link = default_kwargs['amazon_link']
        self.amazon_book_title = default_kwargs['amazon_book_title']
        self.amazon_book_id = default_kwargs['amazon_book_id']
        self.ISBN_13 = default_kwargs['ISBN_13']

        self.is_cached = default_kwargs['is_cached']
        self.opac_link = default_kwargs['opac_link']

        self.num_registered = default_kwargs['num_registered']
        # self.num_available = default_kwargs['num_available']

    def to_dict(self):
        return self.__dict__

    def search_book_in_cache(self, cached_book_lis):
        for cached_book in cached_book_lis:
            if cached_book.amazon_book_title == self.amazon_book_title:
                return cached_book

    def copy_vals_from_cached_book(self, cached_book):
        self.ISBN_13 = cached_book.ISBN_13
        self.opac_link = cached_book.opac_link
        self.num_registered = cached_book.num_registered

    def fetch_ISBN_from_amazon(self):
        res = requests_get_as_fox(self.amazon_link)
        li_tag = BeautifulSoup(res.text, features='lxml').find('b', text='ISBN-13:').find_parent('li')
        try:
            self.ISBN_13 = li_tag.text[-14:]
        except AttributeError:
            self.ISBN_13 = False

    def fetch_opac_link_from_opac(self):
        res = requests_get_as_fox(OPAC.search_page_url, params={'kywd': self.ISBN_13})
        try:
            self.opac_link = OPAC.top_page_url + BeautifulSoup(res.text, features='lxml').find(
                class_=OPAC.class_at_book_lis).find('a').get('href')
        except AttributeError:
            self.opac_link = False
            self.num_registered = 0

    def fetch_reg_num_in_opac(self):
        assert self.opac_link
        res = requests_get_as_fox(self.opac_link)
        cond_classes = BeautifulSoup(res.text, features='lxml').find_all(class_=OPAC.class_of_cond)
        cond_classes = [cond_class for cond_class in cond_classes if cond_class.text != OPAC.text_of_cond_header]
        self.num_registered = len(cond_classes)


class Books:
    def __init__(self):
        if exists_cache():
            with DATA_DIR.joinpath('books.json').open('r') as f:
                self.books_in_cached_wl = [Book(**book_ins_vars_dic) for book_ins_vars_dic in json.load(f)]
        else:
            self.books_in_cached_wl = None

        self.books_in_latest_wl = None

    def check_book_is_cached(self):
        if self.books_in_cached_wl:
            num_new_books = 0
            cached_book_title_lis = [book.amazon_book_title for book in self.books_in_cached_wl]
            for book in self.books_in_latest_wl:
                if book.amazon_book_title in cached_book_title_lis:
                    book.is_cached = True
                else:
                    book.is_cached = False
                    num_new_books += 1
            print(f'{num_new_books} new books!')
        else:
            for book in self.books_in_latest_wl:
                book.is_cached = False

    def get_info_from_cache(self):
        books_has_cache = [book for book in self.books_in_latest_wl if book.is_cached]
        for book in books_has_cache:
            cached_book = book.search_book_in_cache(self.books_in_cached_wl)
            book.copy_vals_from_cached_book(cached_book)

    def fetch_ISBNs(self):
        books_has_no_ISBN = [book for book in self.books_in_latest_wl if not book.ISBN_13]
        print(f"fetching {len(books_has_no_ISBN)} book's ISBN from Amazon...")
        for book in books_has_no_ISBN:
            book.fetch_ISBN_from_amazon()

    def fetch_opac_links(self):
        books_no_cache = [book for book in self.books_in_latest_wl if (not book.is_cached) and book.ISBN_13]
        print(f"fetching {len(books_no_cache)} book's opac link from opac...")
        threads = [Thread(target=book.fetch_opac_link_from_opac) for book in books_no_cache]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        # for book in books_no_cache
        #     book.fetch_opac_link_from_opac()
        #     sleep(1)

    def fetch_reg_nums_in_opac(self):
        books_no_reg_num = [book for book in self.books_in_latest_wl if book.num_registered is None and book.opac_link]
        print(f'fetching how many books are registered from OPAC (about {len(books_no_reg_num)} books)...')
        threads = [Thread(target=book.fetch_reg_num_in_opac) for book in books_no_reg_num]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

    def save_books_as_json(self):
        for book in self.books_in_latest_wl:
            book.is_cached = True
        with DATA_DIR.joinpath('books.json').open('w') as f:
            book_ins_vars_dic_lis = [book.to_dict() for book in self.books_in_latest_wl]
            json.dump(book_ins_vars_dic_lis, f, indent=2, ensure_ascii=False)
