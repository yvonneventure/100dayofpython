from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# price= driver.find_element_by_id("")
# name= driver.find_element_by_name("")

# logo= driver.find_element_by_class_name("")
# documentation_link= driver.find_element_by_css_selector(".documentation-widget a")
# bug_link= driver.find_element_by_xpath('//*[@id="bylineInfo"]')  #right click on the element, then copy,  then you can copy the xpath
# times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
# event_name = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
# events = {}
#
# for n in range(len(times)):
#     events[n] = {
#         "time": times[n].text,
#         "name": event_name[n].text,
#         }
# print(events)
#
#
# #driver.close()  # close a tab
# driver.quit()   # close the browser

s =Service('/Users/Zihan/Development/chromedriver')
driver = webdriver.Chrome(service=s)


driver.get("http://secure-retreat-92358.herokuapp.com")

#times = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
#times.click()
fname = driver.find_element(By.NAME, 'fName')
fname.send_keys("kate")
lname = driver.find_element(By.NAME, 'lName')
lname.send_keys("xu")
email = driver.find_element(By.NAME, 'email')
email.send_keys("xxxyyy@gmail.com")
button = driver.find_element(By.CSS_SELECTOR, '.btn-lg')
button.click()