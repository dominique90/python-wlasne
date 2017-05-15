#!/usr/bin/env python
# -*- coding: utf-8" -*
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

opony = 'dunlop r16'

class AllegroSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        driver.get("https://www.allegro.pl")
        czego_szukasz = driver.find_element_by_xpath("//input[@placeholder='czego szukasz?']")
        czego_szukasz.send_keys(opony)
        przycisk_szukaj = driver.find_element_by_css_selector("input[type=submit]")
        przycisk_szukaj.click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
