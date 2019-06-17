import unittest
from selenium import webdriver


class ServerTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS(
            service_args=[
                '--ignore-ssl-errors=true',
                '--ssl-protocol=any'
            ]
        )
        self.driver.set_window_size(1120, 550)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
