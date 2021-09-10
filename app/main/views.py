from flask import render_template

from . import main

@main.route('/')
def index():
    """
    function to show the homepage of the app
    :return: index page
    """
    return render_template('index.html')