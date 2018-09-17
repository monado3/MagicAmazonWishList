from helpers import add_proj_root_to_syspath

add_proj_root_to_syspath()
from core.cls.amazon import MagicAmazon


def main():
    MagicAmazon.open()


if __name__ == '__main__':
    main()
