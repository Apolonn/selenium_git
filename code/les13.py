from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.implicitly_wait(2)

driver.get("http://localhost:8080/litecart/")

k=0

while k<3:
    value = int(driver.find_element_by_css_selector("span.quantity").get_attribute("textContent"))
    newv = str(value + 1)
    driver.find_element_by_css_selector("div#box-campaign-products a").click()
    driver.find_element_by_css_selector('button[name="add_cart_product"]').click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='quantity'][text()='" + newv + "']")))
    driver.find_element_by_css_selector('div[aria-label="Close"]').click()
    k=k+1

driver.find_element_by_css_selector("#cart").click()

count_prod=int(driver.find_element_by_css_selector("tr.item>td:nth-child(4) input").get_attribute("value"))
while count_prod>0:
    count_prod=count_prod-1
    driver.find_element_by_css_selector("tr.item>td:nth-child(4) input").clear()
    summ=driver.find_element_by_css_selector("#box-checkout-summary>table>tbody>tr:nth-child(1)>td:nth-child(2)").get_attribute("textContent")
    driver.find_element_by_css_selector("tr.item>td:nth-child(4) input").send_keys(count_prod)
    driver.find_element_by_css_selector("i.fa.fa-refresh").click()
    WebDriverWait(driver, 10).until_not(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#box-checkout-summary>table>tbody>tr:nth-child(1)>td:nth-child(2)"), summ))


driver.quit()