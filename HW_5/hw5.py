import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

        self.driver = webdriver.Chrome(options=options, executable_path='C:\\Users\\sadfiz\\PycharmProjects\\pythonProject\\venv\\Scripts\\chromedriver.exe')

    def test_menu(self):
        driver = self.driver
        driver.get("http://www.python.org")
        elems = driver.find_elements_by_css_selector('#success-stories ul li a')
        href_list = []
        name_list = []
        for e in elems:
            href_list.append(e.get_attribute("href"))
            name_list.append(e.get_attribute('innerHTML'))
        for i in range(len(href_list)):
            driver.get(
                href_list[i]
            )
            elem = driver.find_element_by_css_selector('.breadcrumbs')
            self.assertIn("success-stories", elem.get_attribute('innerHTML'))
            self.assertIn(
                name_list[i],
                elem.get_attribute('innerHTML')
            )
            time.sleep(5)