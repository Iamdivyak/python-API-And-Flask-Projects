import requests
# import os
from twilio.rest import Client
# from dotenv import load_dotenv

# load_dotenv("/.env")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY="7FTT3FRMZ4C6KL6F"

NEWS_API_KEY="332ea71f2f1444d789ca76f3f2747191"


# - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_params={
    "function":"TIME_SERIES_DAILY_ADJUSTED",
    "symbol":STOCK,
    "apikey":STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_data = response.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]
yesterday_data = stock_data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

#- Get the day before yesterday's closing stock price

day_before_yesterday_data = stock_data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)
#- Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(difference)

# - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

diff_percent = difference/float(yesterday_closing_price) *100
print(diff_percent)
# - If TODO4 percentage is greater than 5 then print("Get News").
# - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.


if diff_percent > 2:
    news_params = {
        "apiKey": NEWS_API_KEY,
        # "q": "tesla",
        "qInTitle": COMPANY_NAME,
        # "domains":
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"]
    # - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

    news_articles = news_data[:3]
    # print(news_articles)

     ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.

# - Create a new list of the first 3 article's headline and description using list comprehension.

    formatted_articles = [f"Headline: {news_data['title']}. \n Brief: {news_data['description']}" for news_data in news_articles]
    print(formatted_articles)
# - Send each article as a separate message via Twilio.
    account_sid = "AC88da2f9fc5eac277dc66f18265ee1aa9"
    auth_token = "ee44c3ed6489b5381ac4d5c799c16fc0"
    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages \
            .create(
            body=article,
            from_='+16073176928',
            to='+91620210****'
        )
        # print(message.status)





