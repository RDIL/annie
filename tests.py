import unittest
from selenium import webdriver


class ServerTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()

    def test_status(self):
        self.driver.get("127.0.0.1:5000")
        self.assertIn("analytics server online", self.driver.page_source)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
