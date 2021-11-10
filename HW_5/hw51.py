import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from pprint import pprint

from selenium.webdriver.chrome.service import Service


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        # запуск Firefox при начале каждого теста
        p = 'C:\\Users\\sadfiz\\PycharmProjects\\pythonProject\\venv\\Scripts\\chromedriver.exe'
        options = Options()
        options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

        self.driver = webdriver.Chrome(options=options,
                                       executable_path='C:\\Users\\sadfiz\\PycharmProjects\\pythonProject\\venv\\Scripts\\chromedriver.exe')

    def test_about_breadcrumbs(self):
        driver = self.driver
        main_page ="http://www.python.org"
        driver.get(main_page)
        elems = driver.find_elements_by_css_selector('#mainnav ul li')
        pprint(elems)

        elems_with_subtag_ul = []
        for e in elems:
            try:
                e.find_element_by_tag_name('ul')
                print(e.get_attribute('innerHTML'))
                elems_with_subtag_ul.append(e)
            except:
                pass

        elems_with_subtag_ul_a_href = []
        for e in elems_with_subtag_ul:
            a_href_from_ul = e.find_element_by_tag_name('a')
            print(a_href_from_ul.get_attribute('innerHTML'))
            elems_with_subtag_ul_a_href.append(a_href_from_ul)

        correct_hrefs = []
        for e in elems_with_subtag_ul_a_href:
            correct_hrefs.append(e.get_attribute('href'))
        pprint(correct_hrefs)

        for href in correct_hrefs:
            driver.get(href)
            time.sleep(5)
