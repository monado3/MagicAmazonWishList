from core.helper.const import DATA_DIR


def main():
    for data_json in DATA_DIR.glob('*.json'):
        data_json.unlink()


if __name__ == '__main__':
    main()
