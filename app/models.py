class Articles:
    """
    class to define Article objects
    """

    def __init__(self, source: dict, author: str, title: str, description: str,
                 url: str, url_to_image: str, published_at: str):
        """
        method to define Article object properties
        :param source:
        :param author:
        :param title:
        :param description:
        :param url:
        :param url_to_image:
        """
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.url_to_image = url_to_image
        self.published_at = published_at


class NewsSources():
    """
    class to model News Sources objects
    """

    def __init__(self, id: str, name: str, description: str, url: str, category: str, language: str, country: str):
        """
        method to define News Sources properties
        :param id:
        :param name:
        :param description:
        :param url:
        :param category:
        :param language:
        :param country:
        """
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country
