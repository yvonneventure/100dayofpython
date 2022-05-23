### auto-follow companies with less than 10,000 employees in North America

URL="https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22102221843%22%5D&companySize=%5B%22B%22%2C%22C%22%2C%22D%22%2C%22E%22%2C%22F%22%5D&keywords=company&origin=FACETED_SEARCH&sid=BDH"
#https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22102221843%22%5D&companySize=%5B%22B%22%2C%22C%22%2C%22D%22%2C%22E%22%2C%22F%22%5D&keywords=company&origin=FACETED_SEARCH&page=2&sid=4~_
#https://www.linkedin.com/search/results/companies/?companyHqGeo=%5B%22102221843%22%5D&companySize=%5B%22B%22%2C%22C%22%2C%22D%22%2C%22E%22%2C%22F%22%5D&keywords=company&origin=FACETED_SEARCH&page=3&sid=vh8

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
from confidential import ACCOUNT_EMAIL,ACCOUNT_PASSWORD


s =Service('/Users/Zihan/Development/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get(URL)
##sign in
time.sleep(2)
sign_in_button = driver.find_element(By.LINK_TEXT,"Sign in")
sign_in_button.click()
time.sleep(5)
email_field = driver.find_element(By.ID,"username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(By.ID,"password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)
time.sleep(5)
## find companies

follow_list = driver.find_elements(By.CSS_SELECTOR,"li .artdeco-button--secondary")
for button in follow_list:
    if button.text=="Follow":
        button.click()
        time.sleep(2)
    else:
        pass

