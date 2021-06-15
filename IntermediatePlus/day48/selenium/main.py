from selenium import webdriver
from config import BRAVE_PATH, CHROME_DRIVER_PATH, ITEM_URL

options = webdriver.chrome.options.Options()
options.binary_location = BRAVE_PATH
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options=options)

# driver.get(ITEM_URL)
# price_element = driver.find_element_by_id("priceblock_ourprice")
# print(price_element.text)

#######################
# PYTHON.ORG EXAMPLES #
#######################
driver.get("https://www.python.org/")
# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

events_dict = {}

event_ul = driver.find_element_by_xpath('//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
event_li_list = event_ul.find_elements_by_css_selector("li")
count = 0
for li in event_li_list:
    date = li.find_element_by_css_selector("time").get_attribute("datetime").split("T")[0]
    event = li.find_element_by_css_selector("a").text
    event_obj = {
        'time': date,
        'name': event
    }
    events_dict[count] = event_obj
    count += 1
print(events_dict)

# Closes active tab
driver.close()

# Quits entire program
# doesn't work - don't know why
# driver.quit()
