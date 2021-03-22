from selenium import webdriver
driver = webdriver.Chrome('/Users/junp/Downloads/chromedriver')
import time

url = 'https://ssoshib.fhda.edu/idp/profile/cas/login?execution=e1s1'
driver.get(url)

xpath = "//a[@class='btn btn-default']"
click_btn = driver.find_element_by_xpath(xpath)
click_btn.click()

time.sleep(3)

input_username = driver.find_element_by_name("j_username")
input_username.send_keys('20478210')
input_password = driver.find_element_by_name("j_password")
input_password.send_keys('dydzkf2042')
submit = driver.find_element_by_name("_eventId_proceed")
submit.click()


