#!/usr/bin/env python

from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://www.gmail.com")
assert "Gmail" in driver.title

element = driver.find_element_by_id("Email")
element.send_keys('********')
element = driver.find_element_by_id("next").click()

element = driver.find_element_by_id("Passwd")
element.send_keys('******')
element = driver.find_element_by_id("signIn").click()

element = driver.find_element_by_xpath("//div[@class='T-I J-J5-Ji T-I-KE L3']").click()

element = driver.find_element_by_name("to")
element.send_keys("dominik.borkowski@controltec.com.pl")

element = driver.find_element_by_name("subjectbox")
element.send_keys("Test selenium")

element = driver.find_element_by_xpath("//div[@class='Am Al editable LW-avf']")
element.send_keys("Witam, Email zostal wygenerowany automatycznie przez Selenium")

element = driver.find_element_by_xpath("//div[@class='T-I J-J5-Ji aoO T-I-atl L3']").click()

element = driver.find_element_by_xpath("//span[@class='gb_9a gbii']").click()
element = driver.find_element_by_id("gb_71").click()

driver.close()




