from time import sleep
from selenium import webdriver

chrome = webdriver.Chrome()

chrome.get("http://www.baidu.com/s?wd=%E7%A5%A8%E6%88%BF&tn=94150176_hao_pg&ie=utf-8")
# chrome.find_element_by_id("su").click()
chrome.find_element_by_id("img_out_3392279511").click()
sleep(5)
chrome.close()

