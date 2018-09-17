from core.cls.book import Books
from core.feature import fetch_from_OPAC_and_save, make_and_open_wishlist


def main():
    books = Books()
    books.books_in_latest_wl = books.books_in_cached_wl
    fetch_from_OPAC_and_save(books, mode='all')
    make_and_open_wishlist()


if __name__ == '__main__':
    main()
