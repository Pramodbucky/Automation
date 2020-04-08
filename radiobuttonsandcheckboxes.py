from selenium import webdriver
import os
from config1 import *

class RC():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driverlocation = CHROME_WEBDRIVER
        os.environ["webdriver.chrome.driver"] = driverlocation
        driver = webdriver.Chrome(driverlocation)
        driver.maximize_window()    # maximize window
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        bmwradiobut = driver.find_element_by_id("bmwradio")
        bmwradiobut.click()
        benzradiobutton = driver.find_element_by_id("benzradio")
        benzradiobutton.click()
        bmwcheck = driver.find_element_by_id("bmwcheck")
        bmwcheck.click()
        benzcheck = driver.find_element_by_id("benzcheck")
        benzcheck.click()
        print("BMW selected? " + str(bmwradiobut.is_selected()))
        print("BENZ selected? " + str(benzradiobutton.is_selected()))
        print("BMW_ch selected? " + str(bmwcheck.is_selected()))
        print("BENZ_ch selected? " + str(benzcheck.is_selected()))

ff = RC()
ff.test()
