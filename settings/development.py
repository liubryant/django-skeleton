# -*- coding: utf-8 -*-

from common import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG


## Logging

LOG_DIR = SITE_DIR / 'log'
if not LOG_DIR.exists():
    LOG_DIR.makedirs()

FILE_HANDLER = logging.FileHandler(LOG_DIR / 'development.log')
FILE_HANDLER.setFormatter(LOG_FORMATTER)
FILE_HANDLER.setLevel(logging.WARN)
logging.root.addHandler(FILE_HANDLER)
logging.root.setLevel(logging.DEBUG)


## Database

DB_DIR = SITE_DIR / 'db'
if not DB_DIR.exists():
    DB_DIR.makedirs()

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = DB_DIR / 'development.sqlite'
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''


## Caching

CACHE_BACKEND = 'dummy://'
CACHE_MIDDLEWARE_KEY_PREFIX += 'dev_'


## Mail

EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
