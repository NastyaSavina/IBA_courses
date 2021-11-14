import pytest
import time
from selenium import webdriver
from pprint import pprint
# фикстура для запуска браузера перед тестом и закрытия после теста
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


@pytest.fixture()
def browser():
    # запуск Firefox при начале каждого теста (до yield)
    binary = FirefoxBinary(
        "C:\\Users\\sadfiz\\Downloads\\MediaGet Downloads\\FirefoxPortableESR\\App\\Firefox64\\firefox.exe")

    driver = webdriver.Firefox(firefox_binary=binary, executable_path='C:\\Users\\sadfiz\\PycharmProjects\\pythonProject\\venv\\Scripts\\ff\\geckodriver.exe')
    # открытие страницы при начале каждого теста
    page = driver.get('http://www.python.org')
    # передача драйвера для использования в тесте
    yield driver
    # закрытие браузера после теста (после yield)
    #driver.close()

def test_main_menu(browser):
    elems = browser.find_elements_by_css_selector('#mainnav ul li')
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
        browser.get(href)
        time.sleep(5)
