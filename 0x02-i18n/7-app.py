#!/usr/bin/env python3
"""flask app
"""

from flask_babel import Babel, gettext
from flask import Flask, render_template, request, g
from typing import Union, Dict
from pytz import timezone
import pytz.exceptions


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """determines best match language
    """
    locale = request.args.get('locaSle')
    if locale is not None:
        if locale in app.config['LANGUAGES']:
            return locale

    if g.user:
        locale = g.user.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale

    locale = request.headers.get('locale', None)
    if locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


# babel.init_app(app, locale_selector=get_locale)


def get_user() -> Union[dict, None]:
    """returns a user dictionary """
    try:
        user_id = request.args.get('login_as')
        usr = users[int(user_id)]
    except Exception:
        usr = None
    return usr


@app.before_request
def before_request():
    """executed before all other"""
    user = get_user()
    g.user = user


@babel.timezoneselector
def get_timezone():
    """
      returns appropriate timezone
    """
    tzone = request.args.get('timezone', None)
    if tzone:
        try:
            return timezone(tzone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    if g.user:
        try:
            tzone = g.user.get('timezone')
            return timezone(tzone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass


    default_tz = app.config['BABEL_DEFAULT_TIMEZONE']
    return default_tz



@app.route('/')
def index() -> str:
    """renders the template
    """
    return render_template("7-index.html")


if __name__ == '__main__':
    app.run(debug=True)
