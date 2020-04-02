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
        driver.get(baseUrl)

        elementById = driver.find_element(By.ID, "bmwcheck")

        if elementById is not None:
            print("We found an element by Id")

        elementByXpath = driver.find_element(By.XPATH, "//legend[contains(text(),'Radio Button Example')]")

        if elementByXpath is not None:
            print("We found an element by XPATH")

        elementByLinkText = driver.find_element(By.LINK_TEXT, "Practice")

        if elementByLinkText is not None:
            print("We found an element by Link Text")

        classelementlist = driver.find_elements(By.CLASS_NAME,"inputs")
        print(len(classelementlist))

        tagelementlist = driver.find_elements_by_tag_name("tr")
        print(len(tagelementlist))

ff = ByDemo()
ff.test()

