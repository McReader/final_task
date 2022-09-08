from os import curdir, path

ROOT_DIR = path.abspath(path.join(path.dirname(__file__), curdir))
CACHE_FILE = path.join(ROOT_DIR, 'db.json')
