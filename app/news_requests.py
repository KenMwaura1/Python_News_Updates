import requests

from .models import Articles, NewsSources

news_sources_url = None
news_articles_url = None
news_base_url = None
news_sources_articles_url = None
all_news_sources_url = None
api_key = None


def request_config(app):
    """
    function to assign proper values to variables required to make requests to the Api
    :param app:
    :return: values from the config file
    """
    global news_sources_url, news_articles_url, news_base_url, news_sources_articles_url, all_news_sources_url, api_key
    news_sources_url = app.config.get('NEWS_SOURCES_URL')
    news_articles_url = app.config.get('NEWS_ARTICLES_APL_URL')
    news_base_url = app.config.get('NEWS_API_BASE_URL')
    news_sources_articles_url = app.config.get('NEWS_SOURCES_ARTICLES_URL')
    all_news_sources_url = app.config.get('ALL_NEWS_SOURCES')
    api_key = app.config.get('API_KEY')


def process_articles_response(list_articles):
    """
    function to process articles
    :param list_articles:
    :return: list of articles
    """
    list_of_articles = []
    for article in list_articles:
        source = article.get("source")
        author = article.get("author")
        description = article.get("description")
        title = article.get("title")
        url = article.get("url")
        url_to_image = article.get("urlToImage")
        published_at = article.get("publishedAt")

        new_article = Articles(source, author, title,
                               description, url, url_to_image, published_at)
        list_of_articles.append(new_article)

    return list_of_articles


def get_articles(article):
    """
    function to get articles from the News Api
    :param article:
    :return: list of articles
    """
    articles_url = news_articles_url.format(article, api_key)
    with requests.get(articles_url) as url:
        articles_response = url.json()

        list_of_articles = None
        if articles_response['articles']:
            list_of_articles = process_articles_response(articles_response['articles'])

    return list_of_articles


def process_sources_response(list_sources):
    """
    function to process news sources
    :param list_sources:
    :return: list of news sources
    """
    list_of_sources = []
    for source in list_sources:
        id = source.get("id")
        name = source.get("name")
        description = source.get("description")
        url = source.get("url")
        category = source.get("category")
        language = source.get("language")
        country = source.get("country")

        new_source = NewsSources(id, name, description, url, category, language, country)
        list_of_sources.append(new_source)

    return list_of_sources


def get_news_sources(category):
    """
    function to retrieve news sources from the News Api
    :param category:
    :return: list of news sources
    """
    sources_url = news_sources_url.format(category, api_key)

    with requests.get(sources_url) as url:
        sources_response = url.json()

        list_of_sources = None
        if sources_response['sources']:
            list_of_sources = process_sources_response(sources_response['sources'])

    return list_of_sources


def process_all_sources_response(list_of_all_sources):
    """
    function to process all the news sources
    :param list_of_all_sources:
    :return: all the news sources
    """
    sources_list = []
    for source in list_of_all_sources:
        id = source.get("id")
        name = source.get("name")
        description = source.get("description")
        url = source.get("url")
        category = source.get("category")
        language = source.get("language")
        country = source.get("country")

        new_source = NewsSources(id, name, description, url, category, language, country)
        sources_list.append(new_source)

    return sources_list


def get_all_sources():
    """
    get all the news sources
    :return:
    """
    all_sources = all_news_sources_url.format(api_key)

    with requests.get(all_sources) as url:
        all_sources_response = url.json()

        list_of_all_sources = None
        if all_sources_response['sources']:
            list_of_all_sources = process_all_sources_response(all_sources_response['sources'])

    return list_of_all_sources


def process_news_articles(list_of_news_articles):
    """
    function to process news articles from a specified source
    :param list_of_news_articles:
    :return: list of articles
    """
    source_articles = []
    for article in list_of_news_articles:
        source = article.get("source")
        author = article.get("author")
        title = article.get("title")
        description = article.get("description")
        url = article.get("url")
        url_to_image = article.get("urlToImage")
        published_at = article.get("publishedAt")

        new_article = Articles(source, author, title, description, url, url_to_image, published_at)
        source_articles.append(new_article)

    return source_articles


def get_news_sources_articles(source):
    """
    function to retrieve articles from specified sources
    :param source:
    :return: list articles from one source
    """
    articles_url = news_sources_articles_url.format(source, api_key)

    with requests.get(articles_url) as url:
        articles_response = url.json()

        news_articles_source = None

        if articles_response['articles']:
            news_articles_source = process_news_articles(articles_response['articles'])

    return news_articles_source


def process_search_response(search_results):
    """
    function to process search results
    :param search_results:
    :return:
    """
    list_of_results = []
    for article in search_results:
        source = article.get("source")
        author = article.get("author")
        description = article.get("description")
        title = article.get("title")
        url = article.get("url")
        url_to_image = article.get("urlToImage")
        published_at = article.get("publishedAt")

        new_article = Articles(source, author, title,
                               description, url, url_to_image, published_at)
        list_of_results.append(new_article)

    return list_of_results


def search_articles(search_term):
    """
    function to search for articles based on search term
    :param search_term:
    :return: list of results
    """
    search_url = news_articles_url.format(search_term, api_key)

    with requests.get(search_url) as url:
        search_response = url.json()

        search_results = None
        if search_response['articles']:
            search_results = process_search_response(search_response['articles'])

    return search_results
