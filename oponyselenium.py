#!/usr/bin/env python
# -*- coding: utf-8" -*

import unittest
import time
from selenium import webdriver

imie = 'Henryk'
nazwisko = u'Pobożny'
ulica = 'Wawelska'
nr = '1'
kod_pocztowy = '31-619'
miejscowosc = u'Kraków'
nr_tel = '111111111'
email = 'heniuXVI@surge.pl'




class Test_Taking_tires(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_buy_tires_without_registration(self):
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

        my_tires_qan = driver.find_element_by_xpath("//select[@name='_ctTL_r4_ddlQuantity']/option[text()='2 szt.']")
        my_tires_qan.click()
        time.sleep(5)

        buy_button = driver.find_element_by_xpath("//a[@id='_ctTL_r4_bttnATC']")
        buy_button.click()
        time.sleep(5)

        f_button = driver.find_element_by_xpath("//div[@class='button']")
        f_button.click()

        next_button = driver.find_element_by_xpath("//a[@class='linkButton red order']")
        next_button.click()
        time.sleep(5)

        name_field = driver.find_element_by_name('OF_ed_ffDfImie_tb')
        name_field.send_keys(imie)

        surname_field = driver.find_element_by_name('OF_ed_ffDfNazwisko_tb')
        surname_field.send_keys(nazwisko)

        street_field = driver.find_element_by_name('OF_ed_ffDfAdres_tb')
        street_field.send_keys(ulica)

        nr_field = driver.find_element_by_name('OF_ed_ffDfAdresNumer_tb')
        nr_field.send_keys(nr)

        postcode_field = driver.find_element_by_name('OF_ed_ffDfKodPocztowy_tb')
        postcode_field.send_keys(kod_pocztowy)

        city_field = driver.find_element_by_name('OF_ed_ffDfMiejscowosc_tb')
        city_field.send_keys(miejscowosc)

        phone_field = driver.find_element_by_name('OF_ed_ffDwTelefon_ctInp')
        phone_field.send_keys(nr_tel)

        email_field = driver.find_element_by_name('OF_ed_ffDwEmail_tb')
        email_field.send_keys(email)

        checkbox_pay = driver.find_element_by_xpath("//*[@id='_olPT_rix_0']")
        checkbox_pay.click()

        checkbox_credential = driver.find_element_by_xpath("//*[@class='regimen']")
        checkbox_credential.click()
        time.sleep(20)


    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main(verbosity=2)
