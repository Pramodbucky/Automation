from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from config1 import *

class ByDemo():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driverlocation = CHROME_WEBDRIVER
        os.environ["webdriver.chrome.driver"] = driverlocation
        driver = webdriver.Chrome(driverlocation)
        driver.maximize_window()    # maximize window
        driver.get(baseUrl)    # get base url
        title = driver.title    # get title
        print("Title of site: " + title)
        currenturl = driver.current_url    # get current url
        print("Current Url: "+ currenturl)
        driver.refresh()    # refresh browser
        driver.get("https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1")
        driver.back()    # get back page
        print("Backward Pages")
        driver.forward()    # get forward page
        print("Forward pages")
        driver.close()

ff = ByDemo()
ff.test()

