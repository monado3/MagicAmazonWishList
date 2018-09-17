from core.feature import fetch_from_Amazon, fetch_from_OPAC_and_save, make_and_open_wishlist


def main():
    books = fetch_from_Amazon()
    fetch_from_OPAC_and_save(books, mode='newly')
    make_and_open_wishlist()


if __name__ == '__main__':
    main()
