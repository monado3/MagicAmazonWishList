from pathlib import Path

PROJ_DIR = Path(__file__).parents[2]
DATA_DIR = PROJ_DIR.joinpath('data')
WL_DIR = PROJ_DIR.joinpath('wishlist')
JS_DIR = PROJ_DIR.joinpath('javascript')
SAVE_DIR = Path(__file__).parents[1].joinpath('pkls')

START_TAG_FOR_INNER_JSON = f"\n<script type='application/json' id='books.json'>\n"
END_TAG_FOR_INNER_JSON = f"\n</script>\n"

PS_ADDED_TO_WL = f"\n<script src='{JS_DIR.joinpath('magic.js').resolve()}'></script>\n"
