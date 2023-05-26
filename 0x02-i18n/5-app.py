#!/usr/bin/env python3
"""flask app
"""

from flask_babel import Babel, gettext
from flask import Flask, render_template, request, g


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


def get_user(user_id):
    """returns a user dictionary """
    if user_id not in users.keys() or user_id is None:
        return None
    print(users[user_id])
    return users[user_id]


@app.before_request
def before_request():
    """executed before all other"""
    user_id = request.args.get('login_as')
    usr = None
    if user_id is not None:
        usr = get_user(int(user_id))
    if usr is not None:
        g.user = usr
    return None


@app.route('/')
def index():
    """renders the template
    """
    user_name = None
    if hasattr(g, 'user') and isinstance(g.user, dict) and 'name' in g.user:
        user_name = g.user['name']
    not_logged_in = gettext('not_logged_in')
    logged_in_as = gettext('logged_in_as')
    if user_name is not None:
        return render_template('5-index.html', user_name=user_name,
                               logged=logged_in_as)
    return render_template('5-index.html', not_logged=not_logged_in)


if __name__ == '__main__':
    app.run(debug=True)
