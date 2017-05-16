#!/usr/bin/env python
# -*- coding: utf-8" -*

import unittest
from selenium import webdriver

login = 'dominique90@gmail.com'
haslo = 'ramoszenok90'
zle_haslo = 'dupa'



class ZalogujSieMessenger(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_Valid_Registration(self):
        driver = self.driver
        driver.get("http://www.messenger.com")
        email_field = driver.find_element_by_name('email')
        email_field.send_keys(login)
        passwd_field = driver.find_element_by_name('pass')
        passwd_field.send_keys(haslo)
        submit_button = driver.find_element_by_name('login')
        submit_button.click()
        assert u"Wpisz ponownie hasło" not in driver.page_source

    def test_inValid_Registration(self):
        driver = self.driver
        driver.get("http://www.messenger.com")
        email_field = driver.find_element_by_name('email')
        email_field.send_keys(login)
        passwd_field = driver.find_element_by_name('pass')
        passwd_field.send_keys(zle_haslo)
        submit_button = driver.find_element_by_name('login')
        submit_button.click()
        assert "Messenger" in driver.page_source

    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main(verbosity=2)
