import requests

from models import Articles, NewsSources

news_sources_url = None
news_articles_url = None
news_base_url = None
api_key = None


def request_config(app):
    """
    function to assign proper values to variables required to make requests to the Api
    :param app:
    :return: values from the config file
    """
    global news_sources_url, news_articles_url, news_base_url, api_key
    news_sources_url = app.config.get('NEWS_SOURCES_URL')
    news_articles_url = app.config.get('NEWS_ARTICLES_APL_URL')
    news_base_url = app.config.get('NEWS_API_BASE_URL')
    api_key = app.config.get('api_key')


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
        print(articles_response)

        list_of_articles = None
        if articles_response['results']:
            list_of_articles = process_articles_response(articles_response['results'])

    return list_of_articles


def
