STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
import requests
import datetime as dt
import html

from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC6761d771f927f7cedd19c74f38fc9ec8'
auth_token = 'b90dfb1eb19d9e11754de8b507393dde'
client = Client(account_sid, auth_token)

def get_news():
    new_key="3c290a9e097e44c48253b3bd79609c36"
    news=requests.get(url=f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&from={t2}&sortBy=popularity&apiKey={new_key}")
    news.raise_for_status()
    news_data=news.json()
    news_data=news_data["articles"][0]
    return f"Headline: {news_data['title']}: \nBrief: {news_data['description']}"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
alpha_key = "F94YAJI91B638ZI3"
response=requests.get(url=f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={alpha_key}")
response.raise_for_status()
stock_dataset=response.json()
stock_data=stock_dataset["Time Series (Daily)"]
today=dt.datetime.today()
T1=str(dt.datetime.today()-dt.timedelta(days=2))
T2=str(dt.datetime.today()-dt.timedelta(days=3))
t1=T1.split(" ")[0]
t2=T2.split(" ")[0]
print(stock_data)
t1_data=float(stock_data[t1]["4. close"])
t2_data=float(stock_data[t2]["4. close"])
if (t1_data-t2_data)/t2_data>0.01:
    percent=(t1_data-t2_data)/t2_data
    percentage="{0:.1%}".format(percent)
    content=get_news()
    nes=html.unescape(f"TSLA: 🔺{percentage} {content}")

    message = client.messages.create(body=nes,from_='+16204989396',to='+16478839992')

   # print(message.status)

elif (t1_data-t2_data)/t2_data<-0.01:
    percent = (t1_data - t2_data) / t2_data
    percentage = "{0:.1%}".format(percent)
    content = get_news()
    nes = html.unescape(f"TSLA: 🔻{percentage} {content}")

    message = client.messages.create(body=nes, from_='+16204989396', to='+16478839992')

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

