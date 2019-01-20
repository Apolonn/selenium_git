from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

log=[]

class MyListener(AbstractEventListener):
    def before_find(self, by, value, driver):
        log.append(by+value)
    def after_find(self, by, value, driver):
        log.append(by + value + "found")
    def on_exception(self, exception, driver):
        log.append(exception)

driver = EventFiringWebDriver(webdriver.Chrome(), MyListener())


driver.implicitly_wait(2)



driver.get("http://localhost:8080/litecart/admin/?app=catalog&doc=catalog&category_id=1")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin" + Keys.RETURN)

k=driver.find_elements_by_xpath(".//tr/td[./img and ./a]/a")
d=0

while d < len(k):
    k[d].click()
    driver.get("http://localhost:8080/litecart/admin/?app=catalog&doc=catalog&category_id=1")
    k = driver.find_elements_by_xpath(".//tr/td[./img and ./a]/a")
    d=d+1


print(log)

