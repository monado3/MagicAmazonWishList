from core.helper.const import PROJ_DIR, SETTING_CONTENTS, SETTING_FILE_NAME


def main():
    with PROJ_DIR.joinpath(SETTING_FILE_NAME).open('w', encoding='utf-8') as f:
        f.write(SETTING_CONTENTS)


if __name__ == '__main__':
    main()
