from flask import render_template

from . import main
from ..news_requests import get_articles, get_news_sources

@main.route('/')
def index():
    """
    function to show the homepage of the app
    :return: index page
    """
    general_news = get_news_sources('general')
    business = get_news_sources('business')
    tech = get_news_sources('technology')
    sports = get_news_sources('sports')

    return render_template('index.html', general=general_news, business=business, tech=tech, sports=sports)
