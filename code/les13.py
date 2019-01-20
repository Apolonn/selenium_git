from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.implicitly_wait(2)

driver.get("http://localhost:8080/litecart/")

k=0

while k<3:
    value = int(driver.find_element_by_css_selector("span.quantity").get_attribute("textContent"))
    newv = str(value + 1)
    driver.find_element_by_css_selector("li.product").click()
    driver.find_element_by_css_selector('button[name="add_cart_product"]').click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='quantity'][text()='" + newv + "']")))
    driver.get("http://localhost:8080/litecart/")
    k=k+1

driver.find_element_by_css_selector("#cart").click()
allprod=driver.find_elements_by_css_selector("ul.items>li")
lenprod = len(allprod)
cprod=1

while lenprod > 0:
    priceone=driver.find_element_by_css_selector("tr.footer>td:nth-child(2)").get_attribute("textContent")
    d = allprod[0].find_element_by_css_selector("p:nth-child(4)")
    d.click()
    # если позиций больше 1, то ждем пока изменится цена
    if lenprod>1:
        WebDriverWait(driver, 10).until_not(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tr.footer>td:nth-child(2)"), priceone))
    # если позиция одна, ждем до появления текста
    else:
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#checkout-cart-wrapper p:nth-child(1)"),"There are no items in your cart."))
    allprod = driver.find_elements_by_css_selector("ul.items>li")
    lenprod = len(allprod)




driver.quit()