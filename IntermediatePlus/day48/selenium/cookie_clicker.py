import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, \
    ElementNotInteractableException, \
    ElementClickInterceptedException, \
    StaleElementReferenceException
import os.path
from config import BRAVE_PATH, CHROME_DRIVER_PATH

PRODUCT_UPPER_LIM = 19
PRODUCT_LOWER_LIM = -1

valid = False
while not valid:
    game_mode = input("Enter 1 for Auto Mode or 2 for Manual Mode: ")
    if game_mode == '1':
        game_mode = 'AUTO'
        valid = True
    elif game_mode == '2':
        game_mode = 'MANUAL'
        valid = True

print(f"Game mode: {game_mode}")

options = webdriver.chrome.options.Options()
options.binary_location = BRAVE_PATH
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options=options)

driver.get("https://orteil.dashnet.org/cookieclicker/")

cookies = 0
cookie = driver.find_element_by_id("bigCookie")
cookie_counter = driver.find_element_by_id("cookies")

cookie.click()

buy = driver.find_element_by_id("storeBulkBuy")
sell = driver.find_element_by_id("storeBulkSell")

buy_sell_1 = driver.find_element_by_id("storeBulk1")


# Gets save game code from save game textarea
# Saves it to text file
def save_game(this_driver):
    successful = False
    options_btn = this_driver.find_element_by_id("prefsButton")
    try:
        options_btn.click()
    except (NoSuchElementException,
            StaleElementReferenceException,
            ElementNotInteractableException,
            ElementClickInterceptedException):
        return
    export_save = this_driver.find_element_by_link_text("Export save")
    try:
        export_save.click()
    except StaleElementReferenceException:
        options_btn.click()
        print("Problem during game save.\nGame not saved.")
        return
    text_area = this_driver.find_element_by_id("textareaPrompt")
    save_code = text_area.text
    all_done_btn = this_driver.find_element_by_link_text("All done!")
    with open("save_code.txt", mode="w") as file:
        file.write(save_code)
    all_done_btn.click()
    options_btn.click()


# Loads game code from file
# Enters it into load game textarea
def load_game(drive):
    with open("save_code.txt") as file:
        save_code = file.read()
    options_btn = drive.find_element_by_id("prefsButton")
    options_btn.click()
    import_save_btn = drive.find_element_by_link_text("Import save")
    import_save_btn.click()
    text_area = drive.find_element_by_id("textareaPrompt")
    text_area.send_keys(save_code)
    load_btn = drive.find_element_by_link_text("Load")
    load_btn.click()
    options_btn.click()


# Returns current number of cookies as integer
def count_cookies(this_driver):
    current_cookie_str = this_driver.find_element_by_id(
        "cookies").text.split(" ")
    try:
        cookie_count = int(current_cookie_str[0].replace(",", ""))
    except ValueError:
        mil_or_bil = current_cookie_str[1].split("\n")[0]
        if mil_or_bil == 'million':
            cookie_count = int(float(current_cookie_str[0]) * 1000000)
        elif mil_or_bil == 'billion':
            print(current_cookie_str)
            cookie_count = int(float(current_cookie_str[0]) * 1000000000)
            print(cookie_count)
    return cookie_count


def print_cookies_all_time(this_driver):
    stats_btn = this_driver.find_element_by_id("statsButton")
    try:
        stats_btn.click()
    except (NoSuchElementException,
            ElementClickInterceptedException,
            ElementNotInteractableException,
            StaleElementReferenceException):
        pass
    try:
        all_time_cookies = this_driver.find_element_by_xpath(
            "//*[@id=\"menu\"]/div[3]/div[4]")
        print(all_time_cookies.text)
    except (NoSuchElementException,
            ElementClickInterceptedException,
            ElementNotInteractableException,
            StaleElementReferenceException):
        pass
    try:
        stats_btn.click()
    except (NoSuchElementException,
            ElementClickInterceptedException,
            ElementNotInteractableException,
            StaleElementReferenceException):
        pass


# If Saved Game Exists, Load Saved Game
if os.path.isfile("save_code.txt"):
    load_game(driver)

# Declare Timers
timeout = time.time() + 30
one_min = time.time() + 60
five_min = time.time() + 60*5
two_hours = time.time() + 60*120
three_hours = time.time() + 60*180

# Main Game Play Loop
if game_mode != "MANUAL":
    while True:
        # Save game to file every minute
        if time.time() > one_min:
            save_game(driver)
            one_min = time.time() + 60

        # Sometimes the Buy 10 button gets clicked somehow
        # This corrects that scenario
        if buy_sell_1.get_attribute("class") != "storePreButton storeBulkAmount selected":
            buy_sell_1.click()

        # Click any enabled products in order of priority
        if time.time() > timeout:
            # Buy upgrade if available
            try:
                upgrade = driver.find_element_by_id("upgrade0")
                upgrade.click()
            except (NoSuchElementException,
                    StaleElementReferenceException,
                    ElementNotInteractableException,
                    ElementClickInterceptedException):
                pass

            # Buy product if available
            for i in range(PRODUCT_UPPER_LIM, PRODUCT_LOWER_LIM, -1):
                try:
                    element = driver.find_element_by_id(f"product{i}")
                    element.click()
                except (NoSuchElementException,
                        ElementNotInteractableException,
                        ElementClickInterceptedException):
                    pass

            # Reset timeout
            timeout = time.time() + 30
        else:
            # Click any bonus cookies
            try:
                shimmer = driver.find_element_by_css_selector(".shimmer")
                shimmer.click()
            except (NoSuchElementException,
                    ElementClickInterceptedException,
                    ElementNotInteractableException,
                    StaleElementReferenceException):
                pass
            # Click the cookie
            try:
                cookie.click()
            except (NoSuchElementException,
                    ElementClickInterceptedException,
                    ElementNotInteractableException,
                    StaleElementReferenceException):
                pass
        if time.time() > five_min:
            # Print cookies baked all time every five minutes
            print_cookies_all_time(driver)
            five_min = time.time() + 60*5

        # if time.time() > three_hours:
        #     save_game(driver)
        #     break

    # if time.time() > five_min:
    #     cps = driver.find_element_by_id("cookies").text.split(" ")[4]
    #     print(f"Cookies per Second: {cps}")
    #     break

    if game_mode != 'MANUAL':
        driver.close()
else:
    pass
