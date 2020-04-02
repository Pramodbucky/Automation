from selenium import webdriver
import os
import time
from config1 import *

class Skygeek:

    def __init__(self, name):
        self.name = name

    def bulkoperation(self):
        #websiteurl
        skygeektesturl = "http://192.168.1.26:8081/Datahub/Account/Login"
        #driver location on your computer
        driverlocation = CHROME_WEBDRIVER
        os.environ["webdriver.chrome.driver"] = driverlocation
        driver = webdriver.Chrome(driverlocation)
        driver.maximize_window()
        driver.get(skygeektesturl)
        username = driver.find_element_by_id("UserName")
        username.send_keys(SKY_GEEK_LOGIN_USERNAME)
        password = driver.find_element_by_id("Password")
        password.send_keys(SKY_GEEK_LOGIN_PASSWORD)
        login = driver.find_element_by_class_name("btn.btn-primary")
        login.click()
        time.sleep(10)
        if username is not None and password is not None and login is not None:
            print("Login Successfully....")
        else:
            print("Login Failed")
        driver.find_element_by_id("fullTextSearch").send_keys(self.name)
        driver.find_element_by_id("SearchText").click()
        time.sleep(10)
        driver.find_element_by_xpath("//input[@class='productCatalogSelector']").click()
        driver.find_element_by_xpath("//button[@id='catalogVendorProductPricing']").click()
        driver.find_element_by_xpath("//a[@id='btnVendorProductPricing']").click()
        time.sleep(10)
        scroll_to = driver.find_element_by_xpath('//*[@id="hot-bulk-vendor-product"]/div[1]/div/div/div/table/tbody/tr/td[17]')
        driver.execute_script("arguments[0].scrollIntoView();", scroll_to)
        time.sleep(5)
        pricevalue = driver.find_element_by_xpath('//*[@id="hot-bulk-vendor-product"]/div[1]/div/div/div/table/tbody/tr/td[15]')
        print(pricevalue.text)
        driver.execute_script("arguments[0].innerText = '12'", pricevalue)
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="hot-bulk-vendor-product"]/div[1]/div/div/div/table/tbody/tr/td[14]').click()
        driver.find_element_by_xpath("//div[@id='btn-save']").click()
        time.sleep(25)
        msgout = driver.find_element_by_xpath("//body/div[@class='w2']/div[@class='sg-alert-wrapper']/div[@class='alert alert-success']/div[1]").text
        print(msgout)

skygeektest = Skygeek('ewq')
skygeektest.bulkoperation()
