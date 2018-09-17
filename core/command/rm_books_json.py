from core.helper.const import BOOKS_JSON_FILE_NAME, DATA_DIR


def main():
    DATA_DIR.joinpath(BOOKS_JSON_FILE_NAME).unlink()


if __name__ == '__main__':
    main()
