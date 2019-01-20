from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("http://localhost:8080/litecart/admin/?app=countries&doc=countries")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin" + Keys.RETURN)


driver.implicitly_wait(2)

driver.find_element_by_css_selector("div>a.button").click()
t=0
links = driver.find_elements_by_css_selector('form a[target="_blank"]')
for link in links:
    links = driver.find_elements_by_css_selector('form a[target="_blank"]')
    main_window = driver.current_window_handle
    all_windows = driver.window_handles
    links[t].click()
    WebDriverWait(driver, 20).until(EC.number_of_windows_to_be(2))
    all_windows = driver.window_handles
    for k in all_windows:
        if k != main_window:
            driver.switch_to_window(k)
            time.sleep(2)
            driver.close()
    driver.switch_to_window(main_window)
    t=t+1

driver.quit()