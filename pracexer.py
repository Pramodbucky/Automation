from selenium import webdriver
import os
from configlist import *
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
        visitname = driver.find_element_by_css_selector("._1spzot3")
        visitname.send_keys("Nepal")
        clicksomewhere = driver.find_element_by_css_selector("._7p5w4i")
        clicksomewhere.click()
        search = driver.find_element_by_xpath("//div[@class='_h6px0p']//span[@class='_m9v25n']")
        search.click()
        time.sleep(10)
        driver.close()

gg = Automation()
gg.airbnb()


