from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def check_tag(tag):
    if len(driver.find_elements_by_tag_name(tag)) > 0:
        return("тег есть")
    else:
        return("тега нет")

driver = webdriver.Chrome()
driver.get("http://localhost:8080/litecart/admin/login.php")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin" + Keys.RETURN)
time.sleep(5)


big = driver.find_elements_by_css_selector("ul#box-apps-menu>li")
t_b = 0
t_s = 1
while t_b < len(big):
    big[t_b].click()
    big = driver.find_elements_by_css_selector("ul#box-apps-menu>li")
    time.sleep(1)
    print(check_tag("h1"))
    sml = big[t_b].find_elements_by_css_selector("li")
    if len(sml) >= 1:
        while t_s < len(sml):
            big = driver.find_elements_by_css_selector("ul#box-apps-menu>li")
            sml = big[t_b].find_elements_by_css_selector("li")
            sml[t_s].click()
            print(check_tag("h1"))
            t_s = t_s + 1
    big = driver.find_elements_by_css_selector("ul#box-apps-menu>li")
    t_b = t_b + 1
    t_s = 1


