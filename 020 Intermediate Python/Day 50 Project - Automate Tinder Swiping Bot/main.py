from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from confidential import MY_EMAIL, MY_PASSWORD

s =Service('/Users/Zihan/Development/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get("http://www.tinder.com")
######## Login #############
sleep(2)
driver.find_element(By.XPATH, '//*[@id="q939012387"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a').click()
sleep(2)
driver.find_element(By.XPATH, '//*[@id="q-789368689"]/div/div/div[1]/div/div/div[3]/span/div[2]/button').click()

sleep(4)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element(By.XPATH,'//*[@id="email"]')
password = driver.find_element(By.XPATH,'//*[@id="pass"]')

email.send_keys(MY_EMAIL)
password.send_keys(MY_PASSWORD)
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

sleep(5)
########## Click some buttons############

allow_location_button = driver.find_element(By.XPATH,'//*[@id="q-789368689"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()
notifications_button = driver.find_element(By.XPATH,'//*[@id="q-789368689"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()
cookies = driver.find_element(By.XPATH,'//*[@id="q939012387"]/div/div[2]/div/div/div[1]/div[1]/button')
cookies.click()

####### Swipe #########

sleep(7)

for num in range(100):
    sleep(2)
    try:
        pop_up = driver.find_element(By.XPATH, '//*[@id="q939012387"]/div/div[1]/div/div/main/div/div/div[1]/div/div[4]/div/div[2]/button/span/span/svg').click()



        add_app = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/button[2]/span').click()
        sleep(1)
    except NoSuchElementException:
        pass
    finally:

        actions = ActionChains(driver)
        actions.send_keys(Keys.ARROW_LEFT).perform()

driver.quit()