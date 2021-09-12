import unittest
from app.models import NewsSources


class SourcesTest(unittest.TestCase):
    """
    Test class to test the behaviour of the News Sources class
    """

    def setUp(self):
        """
        Method that runs before each other test runs
        """
        self.description = 'echCrunch is a leading technology media property, dedicated to obsessively' \
                           ' profiling startups, reviewing new Internet products, and breaking tech news.'
        self.new_source = NewsSources('techcrunch', 'TechCrunch', self.description,
                                      "https://techcrunch.com", "technology", "en", "us")

    def tearDown(self) -> None:
        """
        method to cleanup new sources
        :return: empty news sources
        """
        self.new_source = None

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, NewsSources))

    def test_initialize(self):
        """
        Test case if News Sources class is appropriately initialized.
         :return: bool True
        :return:
        """
        self.assertTrue(self.new_source.id, "techcrunch")
        self.assertTrue(self.new_source.name, "TechCrunch")
        self.assertTrue(self.new_source.description, self.description)
        self.assertTrue(self.new_source.url, "http://techcrunch.com")
        self.assertTrue(self.new_source.category, "technology")
        self.assertTrue(self.new_source.language, "en")
        self.assertTrue(self.new_source.country, "us")
