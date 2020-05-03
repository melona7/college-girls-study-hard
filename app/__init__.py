from flask import Flask

app = Flask(__name__)

app.config.from_object('config')
app.config.from_envvar('APP_SETTINGS', silent=True)

from app import routes
