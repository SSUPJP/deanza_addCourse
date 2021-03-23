from selenium import webdriver
driver = webdriver.Chrome('/Users/junp/Downloads/chromedriver')
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
import telegram
 


url = 'https://ssoshib.fhda.edu/idp/profile/cas/login?execution=e1s1'
driver.get(url)

xpath = "//a[@class='btn btn-default']"
click_btn = driver.find_element_by_xpath(xpath)
click_btn.click()

time.sleep(2)

input_username = driver.find_element_by_name("j_username")
input_username.send_keys('20478210')
input_password = driver.find_element_by_name("j_password")
input_password.send_keys('dydzkf2042')
submit = driver.find_element_by_name("_eventId_proceed")
submit.click()

time.sleep(4)

xpath = "/html/body/div[1]/div/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div[2]"
registration = driver.find_element_by_xpath(xpath)
registration.click()
time.sleep(0.5)
xpath2 = "/html/body/div[1]/div/div[1]/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[2]/a"
class_search = driver.find_element_by_xpath(xpath2)
class_search.click()

time.sleep(6)

driver.switch_to.window(driver.window_handles[1])

select = Select(driver.find_element_by_tag_name("select"))
select.select_by_index(1)

xpath5 = "/html/body/div[3]/form/input[2]"
submit_term = driver.find_element_by_xpath(xpath5)
submit_term.click()

time.sleep(3)


driver.execute_script("window.scrollTo(0, 900)")

select2 = Select(driver.find_element_by_css_selector('select[name=sel_subj]'))
select2.select_by_visible_text('Mathematics-FD')

xpath6 = "/html/body/div[3]/form/input[17]"
submit_course = driver.find_element_by_xpath(xpath6)
submit_course.click()

xpath7 = "/html/body/div[3]/table[2]/tbody/tr[5]/td[3]/form/input[30]"
submit_courseLevel = driver.find_element_by_xpath(xpath7)
submit_courseLevel.click()

time.sleep(2)

driver.execute_script("window.scrollTo(0, 900)")

seats = driver.find_element_by_xpath('/html/body/div[3]/form/table/tbody/tr[3]/td[13]')
howmany = seats.text

# while howmany == '0':
#     print('seats not available')
#     driver.refresh()
#     time.sleep(2)
#     driver.switch_to.window(driver.window_handles[1])
#     print(howmany)

bot = telegram.Bot('1729976271:AAGXV-JOryhi4TUtapm7xb0Hf0RmhhFA3DU')
bot.send_message('@textmagicme33','Math1c course now available')










