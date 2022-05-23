from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import requests

s =Service('/Users/Zihan/Development/chromedriver')
driver = webdriver.Chrome(service=s)
soup=BeautifulSoup()

form_url="https://docs.google.com/forms/d/e/1FAIpQLScD3jxIxpxozt6nuZSVZho1t5wT8bugBwzQ9lQJK4DwZG8sKA/viewform?usp=sf_link"
zillow_url="https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
    "Accept-Language": "en-US;q=0.9,en;q=0.8"
}

response = requests.get(zillow_url, headers=header)

data = response.text
soup = BeautifulSoup(data, "html.parser")

#print(soup)

all_link_elements = soup.select(".list-card-info a")
all_links = []
for link in all_link_elements:
    href = link["href"]
    #print(href)
    if "http" not in href:
        all_links.append(f"https://www.zillow.com/homedetails{href}")
    else:
        all_links.append(href)

#print(all_links)

all_address_elements = soup.select("a .list-card-addr")
all_addresses = [address.get_text().split(" | ")[-1] for address in all_address_elements]
#print(all_addresses)
all_price_elements = soup.select(".list-card-price")
all_prices = [price.get_text().split("+")[0] for price in all_price_elements if "$" in price.text]
#print(all_prices)

for n in range(len(all_links)):
    driver.get(form_url)

    time.sleep(2)
    address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')

    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    submit_button.click()

