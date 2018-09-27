from core.cls.amazon import MagicAmazon
from setting import AmazonInfo


def main():
    for wl_name in AmazonInfo.book_wishlist_dic.keys():
        ma = MagicAmazon(wl_name)
        ma.open()


if __name__ == '__main__':
    main()
