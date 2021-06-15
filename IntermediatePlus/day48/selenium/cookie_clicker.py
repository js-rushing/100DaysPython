import selenium.common.exceptions
import time
from selenium import webdriver
from config import BRAVE_PATH, CHROME_DRIVER_PATH

options = webdriver.chrome.options.Options()
options.binary_location = BRAVE_PATH
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options=options)

driver.get("http://orteil.dashnet.org/cookieclicker/")

cookies = 0
cookie = driver.find_element_by_id("bigCookie")
cookie_counter = driver.find_element_by_id("cookies")

cookie.click()

buy = driver.find_element_by_id("storeBulkBuy")
sell = driver.find_element_by_id("storeBulkSell")

buy_sell_1 = driver.find_element_by_id("storeBulk1")

cursor = {
    'number': 0,
    'quantity': 0,
    'price': 15
}
grandma = {
    'number': 1,
    'quantity': 0,
    'price': 100
}
farm = {
    'number': 2,
    'quantity': 0,
    'price': 1100
}
mine = {
    'number': 3,
    'quantity': 0,
    'price': 12000
}
factory = {
    'number': 4,
    'quantity': 0,
    'price': 130000
}
bank = {
    'number': 5,
    'quantity': 0,
    'price': 1400000
}
temple = {
    'number': 6,
    'quantity': 0,
    'price': 20000000
}
# while True:
#     cookie.click()
#     cookies = int(cookie_counter.text.split(" ")[0].replace(",", ""))
#     if buy_sell_1.get_attribute("class") != "storePreButton storeBulkAmount selected":
#         buy_sell_1.click()
#
#     if cookies > farm['price'] and farm['quantity'] < 5 and mine['quantity'] < 2:
#         # Buy Farm
#         buy.click()
#         driver.find_element_by_id(f"product{farm['number']}").click()
#         farm['price'] += int(farm['price'] * .1535)
#         farm['quantity'] += 1
#     if cookies > mine['price'] and mine['quantity'] < 5 and factory['quantity'] < 2:
#         # Buy Mine
#         buy.click()
#         driver.find_element_by_id(f"product{mine['number']}").click()
#         mine['price'] += int(mine['price'] * .1535)
#         mine['quantity'] += 1
#         # if mine['quantity'] > 1 and farm['quantity'] > 0:
#         #     sell.click()
#         #     while farm['quantity'] > 0:
#         #         driver.find_element_by_id(f"product{farm['number']}").click()
#         #         farm['quantity'] -= 1
#     if cookies > factory['price'] and factory['quantity'] < 5:
#         # Buy Factory
#         buy.click()
#         driver.find_element_by_id(f"product{factory['number']}").click()
#         factory['price'] += int(factory['price'] * .1535)
#         factory['quantity'] += 1
#         # if factory['quantity'] > 1 and mine['quantity'] > 0:
#         #     sell.click()
#         #     while mine['quantity'] > 0:
#         #         driver.find_element_by_id(f"product{mine['number']}").click()
#         #         mine['quantity'] -= 1
#     if cookies > bank['price'] and bank['quantity'] < 5:
#         # Buy Bank
#         buy.click()
#         driver.find_element_by_id(f"product{bank['number']}").click()
#         bank['price'] += int(bank['price'] * .1535)
#         bank['quantity'] += 1
#         # if bank['quantity'] > 1 and factory['quantity'] > 0:
#         #     sell.click()
#         #     while factory['quantity'] > 0:
#         #         driver.find_element_by_id(f"product{factory['number']}").click()
#         #         factory['quantity'] -= 1
#     if cookies > temple['price'] and temple['quantity'] < 5:
#         # Buy Temple
#         buy.click()
#         driver.find_element_by_id(f"product{temple['number']}").click()
#         temple['price'] += int(temple['price'] * .1535)
#         temple['quantity'] += 1

timeout = time.time() + 5
five_min = time.time() + 60*5
while True:
    try:
        cookie.click()
    except selenium.common.exceptions.ElementClickInterceptedException:
        pass
    if time.time() > timeout:
        cookies = int(cookie_counter.text.split(" ")[0].replace(",", ""))
        try:
            upgrade = driver.find_element_by_id("upgrade0")
            upgrade.click()
        except selenium.common.exceptions.NoSuchElementException:
            pass
        except selenium.common.exceptions.StaleElementReferenceException:
            pass
        except selenium.common.exceptions.ElementNotInteractableException:
            pass
        except selenium.common.exceptions.ElementClickInterceptedException:
            pass
        try:
            shipment = driver.find_element_by_id("product8")
            shipment.click()
        except selenium.common.exceptions.NoSuchElementException:
            pass
        except selenium.common.exceptions.ElementNotInteractableException:
            pass
        except selenium.common.exceptions.ElementClickInterceptedException:
            pass
        try:
            wizard_tower = driver.find_element_by_id("product7")
            wizard_tower.click()
        except selenium.common.exceptions.NoSuchElementException:
            pass
        except selenium.common.exceptions.ElementNotInteractableException:
            pass
        except selenium.common.exceptions.ElementClickInterceptedException:
            pass
        try:
            temple = driver.find_element_by_id("product6")
            temple.click()
        except selenium.common.exceptions.NoSuchElementException:
            pass
        except selenium.common.exceptions.ElementNotInteractableException:
            pass
        except selenium.common.exceptions.ElementClickInterceptedException:
            pass
        try:
            bank = driver.find_element_by_id("product5")
            bank.click()
        except selenium.common.exceptions.NoSuchElementException:
            pass
        except selenium.common.exceptions.ElementNotInteractableException:
            pass
        except selenium.common.exceptions.ElementClickInterceptedException:
            pass
        try:
            factory = driver.find_element_by_id("product4")
            factory.click()
        except selenium.common.exceptions.NoSuchElementException:
            pass
        except selenium.common.exceptions.ElementNotInteractableException:
            pass
        except selenium.common.exceptions.ElementClickInterceptedException:
            pass
        try:
            mine = driver.find_element_by_id("product3")
            mine.click()
        except selenium.common.exceptions.NoSuchElementException:
            pass
        except selenium.common.exceptions.ElementNotInteractableException:
            pass
        except selenium.common.exceptions.ElementClickInterceptedException:
            pass
        try:
            farm = driver.find_element_by_id("product2")
            farm.click()
        except selenium.common.exceptions.NoSuchElementException:
            pass
        except selenium.common.exceptions.ElementNotInteractableException:
            pass
        except selenium.common.exceptions.ElementClickInterceptedException:
            pass
        try:
            grandma = driver.find_element_by_id("product1")
            grandma.click()
        except selenium.common.exceptions.NoSuchElementException:
            pass
        try:
            cursor = driver.find_element_by_id("product0")
            cursor.click()
        except selenium.common.exceptions.NoSuchElementException:
            pass
        timeout = time.time() + 5

    if time.time() > five_min:
        cps = driver.find_element_by_id("cookies").text.split(" ")[4]
        print(f"Cookies per Second: {cps}")
        break

driver.close()
