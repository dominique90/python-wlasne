#!/usr/bin/env python
# -*- coding: utf-8" -*

import unittest
from selenium import webdriver

login = '*******'
haslo = '*******'
zle_haslo = '*******'



class Test_Taking_tires(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_Search_tires(self):
        driver = self.driver
        driver.get("http://www.oponeo.pl")
        search_button = driver.find_element_by_xpath("//div[@class='buttonBox home']")
        search_button.click()
        widht_field = driver.find_element_by_name('_ctTS_ddlDimWidth')
        widht_field.click()
        value_field = driver.find_element_by_xpath("//select[@name='_ctTS_ddlDimWidth']/option[text()='205']")
        value_field.click()
        profile_value = driver.find_element_by_name('_ctTS_ddlDimRatio')
        profile_value.click()
        value_field = driver.find_element_by_xpath("//select[@name='_ctTS_ddlDimRatio']/option[text()='55']")
        value_field.click()
        diameter_field =driver.find_element_by_name('_ctTS_ddlDimDiameter')
        diameter_field.click
        value_field = driver.find_element_by_xpath("//select[@name='_ctTS_ddlDimDiameter']/option[text()='16']")
        value_field.click()
        tires = driver.find_element_by_xpath("//div[@class='cart']")
        tires.click()








if __name__ == "__main__":
    unittest.main(verbosity=2)
