import os
from selenium import webdriver
from configlist import *
from selenium.webdriver.common.by import By

class standardclass:
    def __init__(self, url):
        self.url = url
        driverlocation = CHROME_WEBDRIVER
        os.environ["webdriver.chrome.driver"] = driverlocation
        self.driver = webdriver.Chrome(driverlocation)

    def declaredriver(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)

    def getbyType(self,locatortype):
        locatortype = locatortype.lower()
        if locatortype == "id":
            return By.ID
        elif locatortype == "name":
            return By.NAME
        elif locatortype == "classname":
            return By.CLASS_NAME
        elif locatortype == "xpath":
            return By.XPATH
        elif locatortype == "css":
            return By.CSS_SELECTOR
        else:
            print("Invalid Locators!!!")

    def getelement(self,locator,locatortype='id'):
        try:
            locatortype = locatortype.lower()
            ByType = self.getbyType(locatortype)
            element = self.driver.find_element(ByType,locator)
            if element is not None:
                print("Element found")
                return element
        except Exception as e:
            print(e)


