from email.mime.text import MIMEText

import requests
from bs4 import BeautifulSoup
import smtplib
from pprint import pprint
from config import ITEM_URL, \
    TARGET_PRICE, \
    HEADERS, \
    MAILTRAP_USER, \
    MAILTRAP_PASS, \
    SENDER_ADDRESS, \
    RECEIVER_ADDRESS


def send_email(email, content):
    message = content
    connection = smtplib.SMTP("smtp.mailtrap.io", 2525)
    connection.starttls()
    connection.login(user=MAILTRAP_USER, password=MAILTRAP_PASS)
    connection.sendmail(
        from_addr=SENDER_ADDRESS,
        to_addrs=email,
        msg=message
    )
    connection.close()


res = requests.get(url=ITEM_URL, headers=HEADERS)
soup = BeautifulSoup(res.text, "lxml")
price_block = soup.find(name="span", id="priceblock_ourprice")
price_str = price_block.get_text()
price_num = float(price_str.replace("$", ""))

name_block = soup.find(name="span", id="productTitle")
product_name = name_block.get_text().lstrip().rstrip()

print(f"{product_name} - {price_str}")

if price_num < TARGET_PRICE:
    message = f"Subject: Price Alert!\n\n" \
              f"A product you're tracking -\n\n" \
              f"{product_name}\n\n" \
              f"has dropped below the target price\n" \
              f"It is currently priced at {price_str}\n\n" \
              f"Here is a link to the product\n\n" \
              f"{ITEM_URL}"
    send_email(RECEIVER_ADDRESS, message)
