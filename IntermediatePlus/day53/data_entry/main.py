from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, \
    ElementNotInteractableException, \
    ElementClickInterceptedException, \
    StaleElementReferenceException
from bs4 import BeautifulSoup
import requests
from config import BRAVE_PATH, \
    CHROME_DRIVER_PATH, \
    BS_HEADERS, \
    GOOGLE_FORM_URL, \
    ZILLOW_BASE_URL
from ListCard import ListCard


def fill_form(listing):
    success = False
    options = webdriver.chrome.options.Options()
    options.binary_location = BRAVE_PATH
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options=options)
    driver.get(GOOGLE_FORM_URL)

    address_input = driver.find_element_by_xpath("//*[@id=\"mG61Hd\"]/div[2]/div/div[2]/div[1]"
                                                 "/div/div/div[2]/div/div[1]/div/div[1]/input")
    price_input = driver.find_element_by_xpath("//*[@id=\"mG61Hd\"]/div[2]/div/div[2]/div[2]"
                                               "/div/div/div[2]/div/div[1]/div/div[1]/input")
    link_input = driver.find_element_by_xpath("//*[@id=\"mG61Hd\"]/div[2]/div/div[2]/div[3]"
                                              "/div/div/div[2]/div/div[1]/div/div[1]/input")
    submit_btn = driver.find_element_by_xpath("//*[@id=\"mG61Hd\"]/div[2]/div/div[3]/div[1]"
                                              "/div/div/span/span")

    while not success:
        try:
            address_input.send_keys(listing.address)
            price_input.send_keys(listing.price)
            link_input.send_keys(listing.link)
            submit_btn.click()
            success = True
        except (ElementNotInteractableException,
                ElementClickInterceptedException,
                NoSuchElementException,
                StaleElementReferenceException):
            pass

    driver.close()


res = requests.get(url=ZILLOW_BASE_URL, headers=BS_HEADERS)

soup = BeautifulSoup(res.text, "html.parser")
list_cards = soup.find_all(class_="list-card")
for card in list_cards:
    try:
        this_card = ListCard(card)
        fill_form(this_card)
    except AttributeError:
        pass
