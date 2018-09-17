from core.feature import fetch_from_OPAC_and_save, gen_books_from_cache, make_and_open_wishlist


def main():
    books = gen_books_from_cache()
    fetch_from_OPAC_and_save(books, mode='all')
    make_and_open_wishlist()


if __name__ == '__main__':
    main()
