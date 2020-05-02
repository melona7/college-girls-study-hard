
import os

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

# Secret key for encrypting cookies
SECRET_KEY = b'\xc9\xfd\xb2\x93\xd6\x02\x97\xd5 q\x9c\xc8 \xca{\x85\x18\xeb\xa7b\xd2by\xfd'
SESSION_COOKIE_NAME = 'login'

# Database file is var/insta485.sqlite3
DATABASE_FILENAME = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'var', 'study.sqlite3'
)
