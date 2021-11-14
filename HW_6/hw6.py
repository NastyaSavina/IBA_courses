import pytest
import time
from selenium import webdriver
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


def test_menu(browser):
    elems = browser.find_elements_by_css_selector('#success-stories ul li a')
    href_list = []
    name_list = []
    for e in elems:
        href_list.append(e.get_attribute("href"))
        name_list.append(e.get_attribute('innerHTML'))
    for i in range(len(href_list)):
        browser.get(
            href_list[i]
        )
        elem = browser.find_element_by_css_selector('.breadcrumbs')
        assert("success-stories", elem.get_attribute('innerHTML'))
        assert(
            name_list[i],
            elem.get_attribute('innerHTML')
        )
        time.sleep(5)