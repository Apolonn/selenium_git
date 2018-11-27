from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://localhost:8080/litecart/")
pr=driver.find_element_by_id("popular-products")
fpr=pr.find_elements_by_class_name("product")
count = 0
t = "тайтл есть"
for kek in fpr:
    for stc in (kek.find_elements_by_class_name("sticker")):
        count+=1
        if len(stc.text)<0:
            t="тайтла где-то нет"
    print(count,"стикер,", t)
    count=0

driver.quit()