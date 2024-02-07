#!/usr/bin/env python3
"""initiate a flask app using Babel"""
from datetime import timezone
from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz import timezone
import pytz.exceptions

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """babel config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """get the local selector"""
    lcl = request.args.get('locale', None)
    if lcl and lcl in app.config['LANGUAGES']:
        return lcl
    if g.user:
        lcl = g.user.get('locale')
        if lcl in app.config['LANGUAGES']:
            return lcl

    lcl = request.headers.get('locale', None)
    if lcl and lcl in app.config['LANGUAGES']:
        return lcl
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """a babel time zone selector"""
    tzone = request.args.get('timezone', None)
    if tzone:
        try:
            return timezone(tzone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            return 'UTC'
    if g.user:
        try:
            tzone = g.user.get('timezone')
            return timezone(tzone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            return 'UTC'
    dflt = app.config['BABEL_DEFAULT_TIMEZONE']
    return request.accept_languages.best_match(dflt)


@app.route('/', strict_slashes=False)
def Welcome():
    """a route to a 7-index html"""
    return render_template('7-index.html')


def get_user():
    """returns the user if it is found if not None"""
    user_id = request.args.get('login_as', None)
    if user_id is None:
        return None
    return users.get(int(user_id))


@app.before_request
def before_request():
    """forces this method to be executed before other methods"""
    usr = get_user()
    g.user = usr


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")
