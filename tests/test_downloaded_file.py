from selenium import webdriver
import unittest


class TestDownloadedFile(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test(self):
        self.driver.get('http://localhost:3000')
        assert 'test-file' in self.driver.page_source


if __name__ == "__main__":
    unittest.main()
