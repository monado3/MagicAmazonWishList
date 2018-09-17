from helper import add_proj_root_to_syspath

add_proj_root_to_syspath()
from core.helper.const import DATA_DIR

CACHE_FILE = 'books.json'


def main():
    DATA_DIR.joinpath(CACHE_FILE).unlink()


if __name__ == '__main__':
    main()
