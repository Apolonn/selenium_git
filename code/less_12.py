from time import gmtime, strftime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

import time



driver = webdriver.Chrome()

driver.get("http://localhost:8080/litecart/admin/?app=catalog&doc=catalog")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin" + Keys.RETURN)
time.sleep(5)



dirname = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(dirname, '1.jpg')


name=strftime("product%Y%m%d%H%M%S@mail.ru", gmtime())
code=12345
date_valid_from='01.01.2019'
date_valid_to='01.01.2020'
# path="/Users/anton/Documents/selen_p/selenium_git/code/1.jpg"
sdesc="short_desc"
desc="desc"
attr="attr"
title="title"
meta="meta"
price=22



driver.find_element_by_css_selector('.list-inline.pull-right>li:nth-child(3)').click()
driver.find_element_by_css_selector('div[data-toggle="buttons"]>label:nth-child(1)').click()
driver.find_element_by_name("name[en]").send_keys(name)
driver.find_element_by_name("code").send_keys(code)
driver.find_element_by_name("date_valid_from").send_keys(date_valid_from)
driver.find_element_by_name("date_valid_to").send_keys(date_valid_to)
driver.find_element_by_css_selector('input[type="file"]').send_keys(path)
driver.find_element_by_css_selector('ul.nav-tabs>li:nth-child(2)').click()
time.sleep(2)

driver.find_element_by_name("short_description[en]").send_keys(sdesc)
driver.find_element_by_css_selector('div.input-group div.trumbowyg-editor').send_keys(desc)
driver.find_element_by_name("attributes[en]").send_keys(attr)
driver.find_element_by_name("head_title[en]").send_keys(title)
driver.find_element_by_name("meta_description[en]").send_keys(meta)

driver.find_element_by_css_selector('ul.nav-tabs>li:nth-child(3)').click()
time.sleep(2)
driver.find_element_by_css_selector('input[name="purchase_price"]').clear()
driver.find_element_by_css_selector('input[name="purchase_price"]').send_keys(22)
driver.find_element_by_css_selector('select[name="purchase_price_currency_code"] option[value="USD"]').click()

driver.find_element_by_name("prices[GBP]").send_keys(price)
driver.find_element_by_name("prices[USD]").send_keys(price)
driver.find_element_by_name("prices[EUR]").send_keys(price)


type="submit"
driver.find_element_by_css_selector('button[value="Save"]').click()


elem = driver.find_elements_by_xpath("//*[contains(text(),'" + name + "')]")
if len(elem)>0:
    print("продукт есть")
else:
    print("продута нет")

driver.quit()