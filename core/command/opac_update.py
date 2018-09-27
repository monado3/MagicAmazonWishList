from core.feature import fetch_from_OPAC_and_save, gen_books_from_cache, make_and_open_wishlist
from setting import AmazonInfo


def main():
    for wl_name, wl_link in AmazonInfo.book_wishlist_dic.items():
        books = gen_books_from_cache(wl_name)
        fetch_from_OPAC_and_save(books, mode='all')
        make_and_open_wishlist(wl_name)


if __name__ == '__main__':
    main()
