from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://localhost:8080/litecart/admin/login.php")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin" + Keys.RETURN)
driver.implicitly_wait(5)
driver.get("http://localhost:8080/litecart/admin/?app=countries&doc=countries")


k=driver.find_elements_by_css_selector('form>table>tbody>tr.row')
d=0
dict ={}
while d < len(k):
    k = driver.find_elements_by_css_selector('form>table>tbody>tr.row')
    z = k[d].find_elements_by_css_selector('td')
    dict[z[4].get_attribute("textContent")]=z[5].get_attribute("textContent")
    if int(z[5].get_attribute("textContent")) > 0:
        b = z[4].find_elements_by_css_selector('a')
        b[0].click()
        kk = driver.find_elements_by_css_selector('form>table>tbody>tr>td:nth-child(3)>input')
        dd=0
        list=[]
        while dd < len(kk)-1:
            ff=driver.find_elements_by_css_selector('form>table>tbody>tr>td:nth-child(3)>input')
            list.append(ff[dd].get_attribute("value"))
            dd=dd+1
        driver.get("http://localhost:8080/litecart/admin/?app=countries&doc=countries")
        k = driver.find_elements_by_css_selector('form>table>tbody>tr.row')
        z = k[d].find_elements_by_css_selector('td')
        dict[z[4].get_attribute("textContent")] = list
    d=d+1

driver.get("http://localhost:8080/litecart/admin/?app=geo_zones&doc=geo_zones")
list=[]
dict2={}
d=0
k = driver.find_elements_by_css_selector('form>table>tbody>tr.row')
while d < len(k):
    k = driver.find_elements_by_css_selector('form>table>tbody>tr.row')
    z = k[d].find_elements_by_css_selector('td')
    b = z[2].find_elements_by_css_selector('a')
    b[0].click()
    ddd=0
    elem = driver.find_elements_by_css_selector('form>table>tbody>tr>td:nth-child(3)>select>option[selected="selected"]')
    while ddd<len(elem):
        list.append(elem[ddd].get_attribute("textContent"))
        ddd=ddd+1
    driver.get("http://localhost:8080/litecart/admin/?app=geo_zones&doc=geo_zones")
    k = driver.find_elements_by_css_selector('form>table>tbody>tr.row')
    z = k[d].find_elements_by_css_selector('td')
    b = z[2].find_elements_by_css_selector('a')
    dict2[b[0].get_attribute("textContent")]=list
    list=[]
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
                if nosort[d]!=ded[d]:
                    dict[the_key] = 'сортировка кривая'
                    break
                else:
                    dict[the_key] = 'сортировка соблюдена'
                d=d+1
            d=0
            ded=[]
            nosort = []
    return dict


is_sorted(dict)
is_sorted(dict2)
print(dict)
print(dict2)

driver.quit()