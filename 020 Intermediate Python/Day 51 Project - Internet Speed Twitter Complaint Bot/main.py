from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from confidential import MY_EMAIL, MY_PASSWORD


PROMISED_DOWN = 600
PROMISED_UP = 30

s =Service('/Users/Zihan/Development/chromedriver')

class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")


        go_button = self.driver.find_element(By.CSS_SELECTOR,".start-button a")
        go_button.click()
        sleep(60)
        self.up = self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        print(f"uploade speed {self.up},download speed{self.down}")


    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        sleep(3)
        email = self.driver.find_element(By.CSS_SELECTOR,"input")
        email.send_keys(MY_EMAIL)
        sleep(2)
        email.send_keys(Keys.ENTER)
        sleep(2)
        password = self.driver.find_element(By.NAME, "password")
        #password = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(MY_PASSWORD)
        sleep(2)
        password.send_keys(Keys.ENTER)
        sleep(7)


        tweet_compose = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        sleep(3)
        tweet_button = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()
        sleep(2)
        self.driver.quit()


bot = InternetSpeedTwitterBot(s)
bot.get_internet_speed()
bot.tweet_at_provider()
