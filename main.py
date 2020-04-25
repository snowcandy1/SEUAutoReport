# -- coding: utf-8 --

from config import *
from selenium import webdriver
import os


def send_request(driver, url, params, method='POST'):
    ajax_query = '''
               $.ajax('%s', {
               type: '%s',
               data: %s, 
               crossDomain: true,
               xhrFields: {
                withCredentials: true
               },
               success: function(){}
               });
               ''' % (url, method, params)
    ajax_query = ajax_query.replace(" ", "").replace("\n", "")
    resp = driver.execute_script("return " + ajax_query)
    return resp

print("东南大学信息化自动填报")

browser = webdriver.Chrome()

browser.get("https://newids.seu.edu.cn/authserver/login?service=http://ehall.seu.edu.cn/qljfwapp2/sys/lwReportEpidemicSeu/*default/index.do")

uname = browser.find_element_by_id("username")
upass = browser.find_element_by_id("password")

uname.send_keys(USER_NAME)
upass.send_keys(USER_PASS)

clickBtn = browser.find_element_by_class_name("auth_login_btn")
clickBtn.click()

browser.implicitly_wait(3)

print(browser.current_url)
while not browser.current_url.startswith("http://ehall.seu.edu.cn/qljfwapp2/sys/lwReportEpidemicSeu/*default/index"):
    pass

print(browser.current_url)
'''
addNew = browser.find_elements_by_class_name("mint-button")
addNewBtn = None
for i in addNew:
    if i.text.find("新增") != -1:
        addNewBtn = i
        break
if not addNewBtn:
    print("网页似乎加载失败了……")
    exit(1)
addNewBtn.click()
'''
browser.get("http://ehall.seu.edu.cn/qljfwapp2/sys/lwReportEpidemicSeu/*default/index.do#/add")
browser.implicitly_wait(8)

submits = browser.find_elements_by_class_name("mint-button")
submitBtn = None
for i in submits:
    if i.text.find("提交") != -1:
        submitBtn = i
        break
print("text: ", submitBtn.text)

if not submitBtn:
    print("网页似乎加载失败了……")
    exit(2)
submitBtn.click()


submit_confirm = False
while not submit_confirm:
    submit_confirm = browser.find_element_by_class_name("mint-msgbox-confirm")
submit_confirm.click()

print("已填报，刷新即可看到填报。")

#

browser.implicitly_wait(15)
browser.refresh()
browser.quit()
os.system('pause')
