import unittest
from selenium import webdriver
from subprocess import Popen


class ServerTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.flask_server = Popen(["python3", "-m", "flask", "run"])

    def test_status(self):
        self.driver.get("127.0.0.1:5000")
        self.assertIn("analytics server online", self.driver.page_source)

    def tearDown(self):
        self.driver.quit()
        self.flask_server.kill()

if __name__ == '__main__':
    unittest.main()
