import json
import time
from pyquery import PyQuery as pq
from selenium import webdriver

mobile_emulation = {'deviceName':"Galaxy S5"}
option = webdriver.ChromeOptions()
option.add_experimental_option("mobileEmulation",mobile_emulation)
driver = webdriver.Chrome(chrome_options=option)

driver.get('https://h5.m.taobao.com/mlapp/mytaobao.html?spm=a215s.7406091.toolbar.i2')

frame = driver.find_element_by_css_selector('body > div > iframe')
driver.switch_to_frame(frame)


user = driver.find_element_by_id('username')
print(user)
user.send_keys('your username')
password = driver.find_element_by_id('password')
password.send_keys("your password")
button = driver.find_element_by_id('btn-submit')
time.sleep(1)
button.click()
time.sleep(1)

js = '''
        document.getElementsByClassName("km-dialog-btn")[0].click()
        
    
'''
driver.execute_script(js)
time.sleep(1)
js = '''
    document.getElementById("SM_BTN_1").click()

'''
driver.execute_script(js)
time.sleep(5)
doc = pq(driver.page_source)
valid = doc.find('#SM_TXT_1')
print(valid)
password = driver.find_element_by_id('password')
password.send_keys("your password")
button = driver.find_element_by_id('btn-submit')
time.sleep(1)
button.click()
cookie = driver.get_cookies()
print(cookie)
jsonCookies = json.dumps(cookie)
with open('taobao.json', 'w') as f:
    f.write(jsonCookies)

driver.close()