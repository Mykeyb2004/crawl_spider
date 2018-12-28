import random
import time

from selenium import webdriver

url = 'https://auth.alipay.com/login/index.htm?loginScene=7&goto=https%3A%2F%2Fauth.alipay.com%2Flogin%2Ftaobao_trust_login.htm%3Ftarget%3Dhttps%253A%252F%252Flogin.taobao.com%252Fmember%252Falipay_sign_dispatcher.jhtml%253Ftg%253Dhttps%25253A%25252F%25252Fi.taobao.com%25252Fmy_taobao.htm%25253Fspm%25253Da21bo.2017.754894437.3.5af911d9UQPCtv%252526ad_id%25253D%252526am_id%25253D%252526cm_id%25253D%252526pm_id%25253D1501036000a02c5c3739&params=VFBMX3JlZGlyZWN0X3VybD1odHRwcyUzQSUyRiUyRmkudGFvYmFvLmNvbSUyRm15X3Rhb2Jhby5odG0lM0ZzcG0lM0RhMjFiby4yMDE3Ljc1NDg5NDQzNy4zLjVhZjkxMWQ5VVFQQ3R2JTI2YWRfaWQlM0QlMjZhbV9pZCUzRCUyNmNtX2lkJTNEJTI2cG1faWQlM0QxNTAxMDM2MDAwYTAyYzVjMzczOQ%3D%3D'

driver = webdriver.Chrome()

driver.get(url)

js = '''
    document.querySelector("#J-loginMethod-tabs > li:nth-child(2)").click()
'''
driver.execute_script(js)

user = driver.find_elements_by_name("logonId")[0]
user.send_keys("your user")
password = driver.find_element_by_id("password_rsainput")

password1 = 'your pass'
#缓慢输入
for i in range(password1.__len__()):  #根据你的密码长度设置
    time.sleep(random.random())
    password.send_keys(password1[i])
    print("输入",password1[i])
time.sleep(1)
button = driver.find_element_by_id("J-login-btn")
#一定要等待足够时间才可以
time.sleep(10)
button.click()
