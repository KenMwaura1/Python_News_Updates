import unittest
from app.models import Articles


class ArticlesTest(unittest.TestCase):
    def setUp(self):
        """
      setUp method that will run before every test
      :return: new instance of Article class
      """
        self.new_source = {"id": "techcrunch", "name": "TechCrunch"}
        self.new_title = "PayPal expands the ability to buy, hold and sell cryptocurrency to the U.K"
        self.new_description = "PayPal will now allow users outside the U.S. to buy, hold and sell cryptocurrency for" \
                               "the first time. The company announced today the launch of a new service that will " \
                               "allow customers in the U.K. to select between four types of cryptocurrencies"
        self.new_url = "http://techcrunch.com/2021/08/23/paypal-expands-the-ability-to-buy-hold-and-sell-cryptocurrency-to-the-u-k/"
        self.new_url_to_image = "https://techcrunch.com/wp-content/uploads/2020/11/GettyImages-887657568.jpg?w=600"
        self.new_article = Articles(self.new_source, "Sarah Perez", self.new_title, self.new_description, self.new_url,
                                    self.new_url_to_image, "2021-08-23T13:49:45Z")

    def tearDown(self):
        self.new_article = None

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Articles))

    def test_initialize(self):
        """
         Test case if Articles is appropriately initialized.
         :return: bool True
         """
        self.assertEqual(self.new_article.source, self.new_source)
        self.assertEqual(self.new_article.author, "Sarah Perez")
        self.assertEqual(self.new_article.title, self.new_title)
        self.assertEqual(self.new_article.description, self.new_description)
        self.assertEqual(self.new_article.url, self.new_url)
        self.assertEqual(self.new_article.url_to_image, self.new_url_to_image)
        self.assertEqual(self.new_article.published_at, "2021-08-23T13:49:45Z")


