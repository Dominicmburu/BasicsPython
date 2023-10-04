import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = ""
NEWS_API_KEY = ""

account_sid = ""
auth_token = ""

#TODO 1. - GET YESTERDAY'S CLOSING STOCK PRICE
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)


#TODO 2. - GET THE DAY BEFORE YESTERDAY'S CLOSING STOCK PRICE
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)


#TODO 3. - FIND THE POSITIVE DIFFERENCE BETWEEN 1 AND 2. E,G 40 - 20 - =20, BUT THE POSITIVE DIFFERENCE IS 20
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"


#TODO 4. - WORK OUT THE PERCENTAGE DIFFERENCE IN PRICE B2N CLOSING PRICE YESTERDAY AND CLOSING PRICE THE DAY BEFORE YESTERDAY
diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(diff_percent)


#TODO 5. - IF TODO4 PERCENTAGE IS GREATER THAN PRINT("GET NEWS")
if abs(diff_percent) > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    three_articles = articles[:3]
    print(three_articles)

    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}$\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages.create(
            body="It's going to rain today. Remember to bring an Umbrella",
            from="+245.....",
            to="+254...........",
        )






