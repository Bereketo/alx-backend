#!/usr/bin/env python3
"""basic flask app
"""
from flask import Flask, render_template
import flask
app = Flask(__name__)


@app.route('/')
def index():
    """handles route /
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
