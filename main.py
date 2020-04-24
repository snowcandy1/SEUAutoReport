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

print(send_request(browser, "http://ehall.seu.edu.cn/qljfwapp2/sys/lwReportEpidemicSeu/mobile/dailyReport.do", "{ \"*json\": 1}"))

print("已填报，刷新即可看到填报。")

browser.refresh()

browser.implicitly_wait(15)
browser.quit()
os.system('pause')
