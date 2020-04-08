from selenium.webdriver.support.select import Select
import time
from standard_class import standardclass

class dropdown:
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        sc = standardclass(baseUrl)
        sc.declaredriver()
        dropelement = sc.getelement("carselect")
        element = Select(dropelement)
        element.select_by_value("benz")
        print("Select Benz by value")
        time.sleep(3)
        element.select_by_index(2)
        print("Select Honda by index")
        time.sleep(3)
        element.select_by_visible_text('BMW')
        print("Select BMW by visiable text")

ff = dropdown()
ff.test()