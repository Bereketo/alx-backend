#!/usr/bin/env python3
"""flask app
"""

from flask_babel import Babel, gettext
from flask import Flask, render_template, request


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
    if locale is not None:
        if locale in app.config['LANGUAGES']:
            return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def gettext():
    """renders the template
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
