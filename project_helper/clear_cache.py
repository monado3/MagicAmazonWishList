from core.helpers.consts import DATA_DIR

CACHE_FILE = 'books.json'


def main():
    DATA_DIR.joinpath(CACHE_FILE).unlink()


if __name__ == '__main__':
    main()
