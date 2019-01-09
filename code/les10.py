from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://localhost:8080/litecart/")


name=driver.find_element_by_css_selector('div#box-campaign-products div.name').get_attribute("textContent")
price=k=driver.find_element_by_css_selector('div#box-campaign-products s.regular-price').get_attribute("textContent")
disc=driver.find_element_by_css_selector('div#box-campaign-products strong.campaign-price').get_attribute("textContent")
tag_price=driver.find_element_by_css_selector('div#box-campaign-products s.regular-price').get_attribute("tagName")
col_price=driver.find_element_by_css_selector('div#box-campaign-products s.regular-price').value_of_css_property("color")
tag_disc=driver.find_element_by_css_selector('div#box-campaign-products strong.campaign-price').get_attribute("tagName")
col_desc=driver.find_element_by_css_selector('div#box-campaign-products strong.campaign-price').value_of_css_property("color")
size_desc=driver.find_element_by_css_selector('div#box-campaign-products strong.campaign-price').value_of_css_property("font-size")
size_price=driver.find_element_by_css_selector('div#box-campaign-products s.regular-price').value_of_css_property("font-size")

driver.find_element_by_css_selector("div#box-campaign-products a").click()
time.sleep(2)
name_2=driver.find_element_by_css_selector('div#box-campaign-products div.name').get_attribute("textContent")
price_2=k=driver.find_element_by_css_selector('div#box-campaign-products s.regular-price').get_attribute("textContent")
disc_2=driver.find_element_by_css_selector('div#box-campaign-products strong.campaign-price').get_attribute("textContent")
tag_price_2=driver.find_element_by_css_selector('div#box-campaign-products s.regular-price').get_attribute("tagName")
col_price_2=driver.find_element_by_css_selector('div#box-campaign-products s.regular-price').value_of_css_property("color")
tag_disc_2=driver.find_element_by_css_selector('div#box-campaign-products strong.campaign-price').get_attribute("tagName")
col_desc_2=driver.find_element_by_css_selector('div#box-campaign-products strong.campaign-price').value_of_css_property("color")
size_desc_2=driver.find_element_by_css_selector('div#box-campaign-products strong.campaign-price').value_of_css_property("font-size")
size_price_2=driver.find_element_by_css_selector('div#box-campaign-products s.regular-price').value_of_css_property("font-size")


if name==name_2:
    print('названия одинаковые')
if price==price_2:
    print('цены одинаковые')
if disc==disc_2:
    print('скидки одинаковые')
if tag_price=="S" and tag_price_2=="S":
    print('цены зачеркнуты')
if tag_disc=="STRONG" and tag_disc_2=="STRONG":
    print('скидка жирная')

col_price=col_price.replace('rgba', '').replace('(', '').replace(')', '').split(", ")
col_desc=col_desc.replace('rgba', '').replace('(', '').replace(')', '').split(", ")
col_price_2=col_price_2.replace('rgba', '').replace('(', '').replace(')', '').split(", ")
col_desc_2=col_desc_2.replace('rgba', '').replace('(', '').replace(')', '').split(", ")

if col_price[0]==col_price[1]==col_price[2] and col_price_2[0]==col_price_2[1]==col_price_2[2]:
    print('серые цвета совпадают')

if int(col_desc[1])==int(col_desc[2])==0 and int(col_desc_2[1])==int(col_desc_2[2])==0:
    print('красные цвета совпадают')

size_price=size_price.replace('px', '').replace('.', ',')
size_desc=size_desc.replace('px', '').replace('.', ',')
size_price_2=size_price_2.replace('px', '').replace('.', ',')
size_desc_2=size_desc_2.replace('px', '').replace('.', ',')

if size_price < size_desc and size_price_2 < size_desc_2:
    print("шрифт у скидки больше")

driver.quit()