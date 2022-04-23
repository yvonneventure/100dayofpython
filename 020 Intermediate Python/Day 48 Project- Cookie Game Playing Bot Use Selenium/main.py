from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

s =Service('/Users/Zihan/Development/chromedriver')
driver = webdriver.Chrome(service=s)
# url='https://www.google.com'
# chrome_driver_path = "/Users/Zihan/Development/chromedriver"
#driver = webdriver.Chrome(executable_path=chrome_driver_path)


driver.get("http://orteil.dashnet.org/experiments/cookie/")


check_time = time.time() + 5
click_time = time.time() + 0.1
timeout = time.time() + 60*5

big_cookie = driver.find_element(By.ID, "cookie")

all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
items_prices = []
store = driver.find_elements(By.CSS_SELECTOR, "#store div")
for price in all_prices:
    price_cost = price.text.split("-")
    items_prices.append(price_cost)

items_prices = items_prices[:-1]
price_list = [item[1] for item in items_prices]
price_int = [int(price.replace(',', '')) for price in price_list] # money_element = money_element.replace(",", "")

store = driver.find_elements(By.CSS_SELECTOR, "#store div")

items_ids = [item.get_attribute('id') for item in store]
print(items_ids)
my_dict = dict(zip(price_int, items_ids))
print(my_dict)

def find_and_click(to_select):
    to_click_on = driver.find_element(By.ID, to_select)
    to_click_on.click()

while True:
    big_cookie.click()
    if time.time() > check_time:
        money_earned = int(driver.find_element(By.ID, "money").text)

        try:
            for price in price_int:
                afford = []
                if price < money_earned:
                    afford.append(price)
                    most_affordable = afford[-1]
        except IndexError:
            pass
        else:
            to_select = my_dict[most_affordable]
            find_and_click(to_select)
        finally:
            check_time = time.time() + 5

# after five mins:
    if time.time() > timeout:
        cookies_per_second = driver.find_element(By.ID, "cps").text
        print(f"this is mine {cookies_per_second}")
        break
