import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

load_dotenv("/Users/yizhigai/Desktop/python_environment_variables/.env")

# get stock data
parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "outputsize": "compact",
    "apikey": os.getenv("ALPHAVANTAGE_API_KEY")
}
response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
time_data = response.json()["Time Series (Daily)"]
close_price = [float(val["4. close"]) for (_, val) in time_data.items()]
data_date = [key for (key, _) in time_data.items()]
yesterday_close_price = close_price[0]

day_before_yesterday_close_price = close_price[1]

difference = yesterday_close_price - day_before_yesterday_close_price
is_increase = True if difference > 0 else False
positive_difference = abs(difference)

percentage_difference = positive_difference / yesterday_close_price * 100

news_trigger = False
if percentage_difference > 1:
    news_trigger = True

# if stock variation hit a limit fetch news
if news_trigger:
    news_parameter = {
        "qInTitle": COMPANY_NAME,
        "from": data_date[1],
        "to": data_date[0],
        "sortBy": "relevancy",
        "language": "en",
        "pageSize": 10,
        "apiKey": os.getenv("NEWS_API")
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameter)
    articles_list = news_response.json()["articles"]

    select_articles = articles_list[:3]

    article_headline_list = [article["title"] for article in select_articles]
    article_description_list = [article["description"] for article in select_articles]

    # send news message through twilio
    client = Client(os.getenv("ACCOUNT_SID"), os.getenv("AUTH_TOKEN"))
    for i in range(0, len(article_description_list)):
        arrow = "🔺" if is_increase else "🔻"
        message_content = f"{STOCK_NAME}: {arrow}{round(percentage_difference, 2)}%\n " \
                          f"Headline: {article_headline_list[i]}\n" \
                          f"Brief: {article_description_list[i]}"
        message = client.messages \
            .create(
            body=message_content,
            from_=os.getenv("FROM_PHONE_NUMBER"),
            to=os.getenv("TO_PHONE_NUMBER")
        )
        print(message.status)
