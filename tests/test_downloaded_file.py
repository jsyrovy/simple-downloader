import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestDownloadedFile(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)

    def tearDown(self):
        self.driver.close()

    def test(self):
        self.driver.get('http://localhost:3000')
        assert 'test-file' in self.driver.page_source


if __name__ == "__main__":
    unittest.main()
