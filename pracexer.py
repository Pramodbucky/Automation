from selenium import webdriver
import os
from config1 import *
from selenium.webdriver.support.select import Select
import time

class Automation:
    def airbnb(self):
        baseUrl = "https://www.airbnb.com/"
        driverlocation = CHROME_WEBDRIVER
        os.environ["webdriver.chrome.driver"] = driverlocation
        driver = webdriver.Chrome(driverlocation)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        visitname = driver.find_element_by_id("Koan-magic-carpet-koan-search-bar__input")
        visitname.send_keys("Nepal")
        time.sleep(5)
        checkin = driver.find_element_by_id("checkin_input")
        checkin.send_keys("Tue, Apr 7")
        time.sleep(5)
        checkout = driver.find_element_by_id("checkout_input")
        checkout.send_keys("Fri, Apr 10")
        time.sleep(5)
        # guestdd = driver.find_element_by_id("lp-guestpicker")
        # guestsel = Select(guestdd)
        # guestsel.select_by_index(0)
        # time.sleep(5)
        search = driver.find_element_by_xpath("//button//span[text()='Search']")
        search.click()
        time.sleep(10)
        driver.close()

gg = Automation()
gg.airbnb()


