from flask import render_template

from . import main
from ..news_requests import get_articles, get_news_sources, get_news_sources_articles, get_all_sources


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


@main.route('/articles/<id>')
def news_source_articles(id):
    """
    function to display articles from a specified news source
    :param id:
    :return: template with source articles
    """
    source = id
    all_source_articles = get_news_sources_articles(id)
    return render_template("article-sources.html", source=source, all_source_articles=all_source_articles)


@main.route('/News-Sources')
def news_sources():
    """
    function to display all news sources
    :return: template of news sources
    """
    all_news_sources = get_all_sources()
    return render_template("news_sources.html", all_news_sources=all_news_sources)
