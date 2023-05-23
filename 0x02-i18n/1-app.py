#!/usr/bin/env python3
"""Babel setup
"""

from flask_babel import Babel
from flask import Flask, render_template
import pytz

app = Flask(__name__)
bable = Babel(app)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'fr']
app.config['TIMEZONE'] = 'UTC'


class Config:
    """config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """renders the template
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
