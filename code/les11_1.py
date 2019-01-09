from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://localhost:8080/litecart/admin/login.php")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin" + Keys.RETURN)
time.sleep(5)
driver.get("http://localhost:8080/litecart/admin/?app=countries&doc=countries")


time.sleep(2)
k=driver.find_elements_by_css_selector('table.data-table > tbody> tr')
d=0
dict ={}
while d < len(k):
    k = driver.find_elements_by_css_selector('table.data-table > tbody> tr')
    z = k[d].find_elements_by_css_selector('td')
    dict[z[4].get_attribute("textContent")]=z[5].get_attribute("textContent")
    if int(z[5].get_attribute("textContent")) > 0:
        b = z[4].find_elements_by_css_selector('a')
        b[0].click()
        time.sleep(2)
        kk = driver.find_elements_by_css_selector('table.data-table > tbody> tr')
        dd=0
        list=[]
        while dd < len(kk):
            zz = kk[dd].find_elements_by_css_selector('td')
            input = zz[2].find_elements_by_css_selector('input')
            list.append(input[0].get_attribute("value"))
            dd=dd+1
        driver.get("http://localhost:8080/litecart/admin/?app=countries&doc=countries")
        k = driver.find_elements_by_css_selector('table.data-table > tbody> tr')
        z = k[d].find_elements_by_css_selector('td')
        dict[z[4].get_attribute("textContent")] = list
        time.sleep(2)
    d=d+1

driver.get("http://localhost:8080/litecart/admin/?app=geo_zones&doc=geo_zones")
time.sleep(2)
list=[]
dict2={}
d=0
k = driver.find_elements_by_css_selector('table.data-table > tbody> tr')
while d < len(k):
    k = driver.find_elements_by_css_selector('table.data-table > tbody> tr')
    z = k[d].find_elements_by_css_selector('td')
    b = z[2].find_elements_by_css_selector('a')
    b[0].click()
    kkk = driver.find_elements_by_css_selector('table.data-table > tbody> tr')
    ddd=0
    while ddd<len(kkk):
        zzz = kkk[ddd].find_elements_by_css_selector('td')
        input = zzz[1].find_elements_by_css_selector('input')
        list.append(input[0].get_attribute("value"))
        ddd=ddd+1
    time.sleep(2)
    driver.get("http://localhost:8080/litecart/admin/?app=geo_zones&doc=geo_zones")
    k = driver.find_elements_by_css_selector('table.data-table > tbody> tr')
    z = k[d].find_elements_by_css_selector('td')
    b = z[2].find_elements_by_css_selector('a')
    dict2[b[0].get_attribute("textContent")]=list
    list=[]
    time.sleep(2)
    d=d+1


def is_sorted(dict):
    nosort = []
    ded = []
    d = 0
    for the_key, the_value in dict.items():
        if len(the_value) <=1:
            dict[the_key]='один элемент'
        else:
            for x in the_value:
                nosort.append(x)
                ded.append(x)
            ded.sort()
            while d<len(nosort):
                if nosort[0]!=ded[0]:
                    dict[the_key] = 'сортировка кривая'
                d=d+1
            d=0
            ded=[]
            nosort = []
    return dict
is_sorted(dict)
is_sorted(dict2)
print(dict)
print(dict2)