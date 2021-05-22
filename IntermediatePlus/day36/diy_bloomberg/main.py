import requests
from twilio.rest import Client
from config import STOCK_API_KEY, NEWS_API_KEY, ACCOUNT_SID, AUTH_TOKEN, TWILIO_NUMBER, PERSONAL_NUMBER

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_URL = "https://www.alphavantage.co/query"
STOCK_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}
NEWS_API_URL = "https://newsapi.org/v2/everything"
NEWS_PARAMS = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME,
    "sortBy": "publishedAt",
    "pageSize": 3
}
UP = "🔺"
DOWN = "🔻"


def get_news():
    news_res = requests.get(NEWS_API_URL, NEWS_PARAMS)
    news_data = news_res.json()
    return news_data


# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and
# the day before yesterday then print("Get News").
stock_res = requests.get(STOCK_API_URL, params=STOCK_PARAMS)
stock_data = stock_res.json()
date_keys_list = list(stock_data['Time Series (Daily)'].keys())
today_close = float(stock_data['Time Series (Daily)'][date_keys_list[0]]['4. close'])
previous_close = float(stock_data['Time Series (Daily)'][date_keys_list[1]]['4. close'])
delta_percentage = int((abs(previous_close - today_close) / previous_close) * 100)

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if delta_percentage >= 5:
    news = get_news()
else:
    news = None

# For Testing
# news = get_news()

# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's
# title and description to your phone number.
title_desc_list = []
if news:
    for article in range(len(news['articles'])):
        title_desc_list.append((news['articles'][article]['title'],
                                news['articles'][article]['description']))

    if today_close > previous_close:
        message_header = f"TSLA: {UP}{delta_percentage}%"
    else:
        message_header = f"TSLA: {DOWN}{delta_percentage}%"
    for item in title_desc_list:
        headline = f"Headline: {item[0]}"
        brief = f"Brief: {item[1]}"
        message = f"{message_header}\n{headline}\n{brief}"
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        client.messages.create(body=message, from_=TWILIO_NUMBER, to=PERSONAL_NUMBER)
