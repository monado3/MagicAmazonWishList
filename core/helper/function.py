import pickle

import requests

from core.helper.const import DATA_DIR, SAVE_DIR


def exists_cache():
    if DATA_DIR.joinpath('books.json').exists():
        print('found cache file')
        return True
    else:
        print('no cache file')
        return False


def requests_get_as_fox(url, params=None, **kwargs):
    headers = {'User-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0'}
    res = requests.get(url, params=params, headers=headers, **kwargs)
    res.raise_for_status()
    return res


def pickle_save(obj, filename):
    with SAVE_DIR.joinpath(filename).open('wb') as f:
        pickle.dump(obj, f)


def pickle_load(filename):
    with SAVE_DIR.joinpath(filename).open('rb') as f:
        return pickle.load(f)
