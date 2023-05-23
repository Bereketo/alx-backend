#!/usr/bin/env python3
"""flask app
"""

from flask_babel import Babel
from flask import Flask, render_template, request
import pytz


class Config:
    """config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """determines best match language
    """
    locale = request.args.get('locale')
    if locale is in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """renders the template
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
