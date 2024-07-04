import time
import unittest
from selenium import webdriver
from Functions.OrangePage import paginaLogin

class TestOrangeLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test1(self):
        driver = self.driver
        og = paginaLogin(driver)
        og.login()

        time.sleep(5)

if __name__ == "__main__":
    unittest.main()