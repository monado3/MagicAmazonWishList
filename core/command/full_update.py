from core.feature import fetch_from_Amazon, fetch_from_OPAC_and_save, make_and_open_wishlist
from setting import AmazonInfo


def main():
    for wl_name, wl_link in AmazonInfo.book_wishlist_dic.items():
        books = fetch_from_Amazon(wl_name, wl_link)
        fetch_from_OPAC_and_save(books, mode='all')
        make_and_open_wishlist()


if __name__ == '__main__':
    main()
