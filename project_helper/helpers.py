import sys
from pathlib import Path


def add_proj_root_to_syspath():
    sys.path.append(str(Path(__file__).parents[1].resolve()))
