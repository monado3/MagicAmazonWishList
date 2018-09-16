from pathlib import Path

SETTING_FILE = 'settings.py'
SETTING_CONTENTS = (
'''class AmazonInfo:
    book_wishlist_share_link = 'please input your wishlist url for share'
'''
)


def main():
    base_dir = Path(__file__).parents[1]
    p_setting = base_dir.joinpath(SETTING_FILE)
    with p_setting.open('w', encoding='utf-8') as f:
        f.write(SETTING_CONTENTS)


if __name__ == '__main__':
    main()
