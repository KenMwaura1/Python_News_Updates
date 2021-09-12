from flask import render_template, request, redirect, url_for

from . import main
from ..news_requests import get_articles, get_news_sources, get_news_sources_articles, get_all_sources, search_articles


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

    search = request.args.get('article-query')
    if search:
        return redirect(url_for('main.search_article', article_search=search))

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


@main.route('/News-Articles')
def news_articles():
    """
    function to render new articles
    :return: template with new articles
    """
    tech = get_articles('technology')
    science = get_articles('science')
    health = get_articles('health')
    return render_template("articles.html", tech=tech, science=science, health=health)


@main.route('/News-Sources')
def news_sources():
    """
    function to display all news sources
    :return: template of news sources
    """
    all_news_sources = get_all_sources()
    return render_template("news_sources.html", all_news_sources=all_news_sources)


@main.route('/search/<string:article_search>')
def search_article(article_search: str):
    """
    function that returns search results
    :param article_search:
    :return:
    """
    search_term = article_search.split(" ")
    search_term_format = "+".join(search_term)
    search_results = search_articles(search_term_format)
    return render_template("search_results.html", search_results=search_results)
