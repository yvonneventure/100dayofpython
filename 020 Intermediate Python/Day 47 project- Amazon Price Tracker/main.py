import requests
import lxml
import smtplib
from bs4 import BeautifulSoup

url = "https://www.amazon.ca/Instant-Pot-Duo-Plus-Programmable/dp/B01NBKTPTS/ref=sr_1_2?crid=3H5LQWMRSRJZD&keywords=instant%2Bpot&qid=1650404279&sprefix=in%2Caps%2C412&sr=8-2&th=1"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup)
price = float(soup.find(name="span", class_="a-price-whole").get_text()+soup.find(name="span", class_="a-price-fraction").get_text())

title = soup.find(name="span", class_="a-size-large product-title-word-break").get_Text()

BUY_PRICE = 200

if price < BUY_PRICE:
    message = f"Instant pot is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIl, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
