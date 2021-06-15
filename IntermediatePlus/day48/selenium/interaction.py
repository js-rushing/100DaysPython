from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from config import BRAVE_PATH, CHROME_DRIVER_PATH

WIKI_URL = "https://en.wikipedia.org/wiki/Main_Page"
LAB_URL = "https://secure-retreat-92358.herokuapp.com/"


options = webdriver.chrome.options.Options()
options.binary_location = BRAVE_PATH
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options=options)

#################
# WIKI EXAMPLES #
#################
# driver.get(WIKI_URL)
# print(driver.find_element_by_id("articlecount").find_element_by_css_selector("a").text)
# article_count = driver.find_element_by_css_selector("#articlecount a")
# article_count.click()

# all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

# search = driver.find_element_by_name("search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

driver.get(LAB_URL)
fName = driver.find_element_by_name("fName")
lName = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")
sign_up = driver.find_element_by_css_selector("button")

fName.send_keys("John")
lName.send_keys("Doe")
email.send_keys("jdoe@email.com")
sign_up.click()


# driver.close()
