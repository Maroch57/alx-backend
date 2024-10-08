#!/usr/bin/env python3
"""module: 0-app
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    """main landing page"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
