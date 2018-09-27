import pickle
from threading import Thread
from time import sleep
from typing import List

import requests

from core.helper.const import DATA_DIR, SAVE_DIR, get_json_name


def exists_cache(wl_name: str):
    if DATA_DIR.joinpath(get_json_name(wl_name)).exists():
        print('found cache file')
        return True
    else:
        print('no cache file')
        return False


def requests_get_as_fox(url: str, params=None, **kwargs):
    headers = {'User-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0'}
    res = requests.get(url, params=params, headers=headers, **kwargs)
    res.raise_for_status()
    return res


def is_all_update(mode: str):
    if mode == 'all':
        return True
    elif mode == 'newly':
        return False
    elif isinstance(mode, str):
        raise ValueError("mode should be 'all' or 'newly'")
    else:
        raise TypeError("mode type should be str")


def thread_lis_executioner(thread_lis: List[Thread], interval_sec: int = 0):
    for thread in thread_lis:
        thread.start()
        sleep(interval_sec)
    for thread in thread_lis:
        thread.join()


# for development
def pickle_save(obj: object, filename: str):
    with SAVE_DIR.joinpath(filename).open('wb') as f:
        pickle.dump(obj, f)


def pickle_load(filename: str):
    with SAVE_DIR.joinpath(filename).open('rb') as f:
        return pickle.load(f)
