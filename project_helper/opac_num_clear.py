from helpers import add_proj_root_to_syspath

add_proj_root_to_syspath()
from core.helper.const import DATA_DIR


def main():
    pass

    # with DATA_DIR.joinpath('books.json').open('w') as f:
    #     book_ins_vars_dic_lis = [book.to_dict() for book in self.books_in_latest_wl]
    #     json.dump(book_ins_vars_dic_lis, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    main()
