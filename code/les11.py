from time import gmtime, strftime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://localhost:8080/litecart/create_account")


mail=strftime("user%Y%m%d%H%M%S@mail.ru", gmtime())
name='Ivan'
sname='Ivanov'
pas='user'
postcode=12345



k=driver.find_elements_by_css_selector('form[name="customer_form"]')
b=k[0].find_element_by_css_selector('input[name="firstname"]').send_keys(name)
b=k[0].find_element_by_css_selector('input[name="lastname"]').send_keys(sname)
b=k[0].find_element_by_css_selector('input[name="email"]').send_keys(mail)
b=k[0].find_element_by_css_selector('input[name="postcode"]').send_keys(postcode)
b=k[0].find_element_by_css_selector('input[name="password"]').send_keys(pas)
b=k[0].find_element_by_css_selector('input[name="confirmed_password"]').send_keys(pas)
b=k[0].find_element_by_css_selector('select[name="country_code"] option[value="US"]').click()
time.sleep(2)
k=driver.find_elements_by_css_selector('form[name="customer_form"]')
b=k[0].find_element_by_css_selector('select[name="zone_code"] option[value="CA"]').click()
time.sleep(2)
b=k[0].find_element_by_css_selector('button[value="Create Account"]').click()
driver.find_element_by_css_selector('li.account.dropdown').click()
k=driver.find_elements_by_css_selector('li.account.dropdown.open>ul>li')
k[2].click()

driver.find_element_by_css_selector('li.account.dropdown').click()
driver.find_element_by_css_selector('input[name="email"]').send_keys(mail)
driver.find_element_by_css_selector('input[name="password"]').send_keys(pas)
driver.find_element_by_css_selector('button[name="login"]').click()

driver.find_element_by_css_selector('li.account.dropdown').click()
k=driver.find_elements_by_css_selector('li.account.dropdown.open>ul>li')
k[2].click()

driver.quit()