import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


@pytest.fixture()
def driver():
    # запуск Firefox при начале каждого теста (до yield)
    binary = FirefoxBinary(
        "C:\\Users\\sadfiz\\Downloads\\MediaGet Downloads\\FirefoxPortableESR\\App\\Firefox64\\firefox.exe")

    driver = webdriver.Firefox(firefox_binary=binary, executable_path='C:\\Users\\sadfiz\\PycharmProjects\\pythonProject\\venv\\Scripts\\ff\\geckodriver.exe')

    return driver


def test_calc(driver):
    driver.get('https://kalk.pro/finish/wallpaper/')
    driver.maximize_window()
    # открытие страницы при начале каждого теста

    # браузер ждет 5 сек
    driver.implicitly_wait(5)
    # Необходимо кликнуть мышкой по любому полю страницы, для того, чтобы расчет начал работать.
    body = driver.find_element(By.CLASS_NAME, 'body')
    # перемещаем курсор к элементу body и через 1 сек кликаем по нему
    ActionChains(driver).move_to_element(
        body).pause(1).click().perform()
    # ожидаем полной прогрузки страницы, для этого ждём пока не исчезнет элемент с заданным локатором
    wait(driver, 60).until(
        expected_conditions.invisibility_of_element(
            (By.CLASS_NAME, 'js--modal-app-loading')))
    # Ищем кнопку, которая свернёт рекламу внизу экрана
    elems = driver.find_elements(By.CLASS_NAME, 'i-chevron-down')

    # Если кнопка найдена, то кликаем на неё
    if len(elems) != 0:
        elems[0].click()

    driver.close()
    # self.driver.implicitly_wait(15)

# тестируем кнопочный калькулятор
def test_value(driver):
    driver.get('https://kalk.pro/finish/wallpaper/')
    # открываем калькулятор
    driver.implicitly_wait(5)

    # Необходимо кликнуть мышкой по любому полю страницы, для того, чтобы расчет начал работать.
    # Берем тег Body
    body = driver.find_element(By.CLASS_NAME, 'body')
    # перемещаем курсор к элементу body и через 1 сек кликаем по нему
    ActionChains(driver).move_to_element(
        body).pause(1).click().perform()
    # ожидаем полной прогрузки страницы, для этого ждём пока не исчезнет элемент с заданным локатором
    wait(driver, 60).until(
        expected_conditions.invisibility_of_element(
            (By.CLASS_NAME, 'js--modal-app-loading')))
    elem = driver.find_element(By.CSS_SELECTOR, ".js--onclick-callCalc")
    elem.click()
    # ждем, пока калькулятор откроется
    time.sleep(5)

    for i in range(10):
        print("Нажатие кнопки ", str(i), ": ")
        elem = driver.find_element(By.NAME, str(i))
        elem.click()
        print("OK")
    # проверяем изображение на дисплее
    # (ноль не будет отображаться перед 1)
    elem = driver.find_element(By.CLASS_NAME, "display-indicator-ceils")
    assert elem.text == '123456789'
    driver.close()





