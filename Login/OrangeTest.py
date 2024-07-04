import unittest
from selenium import webdriver
from orangFunctions import funcionesGlobales
from orangePage import paginaLogin

class TestOrangeLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test1(self):
        driver = self.driver
        og = paginaLogin(driver)
        og.login()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()