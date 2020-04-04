import selenium
from selenium import webdriver
import sys
import pprint
import time
from selenium.webdriver.common.keys import Keys

'''
pprint.pprint(sys.path[0])
sys.path.insert(0, 'D:\\00_Tool\\web_driver\\chromedriver_win32')
pprint.pprint(sys.path[0])
'''

USER_UID = '工號'
USER_PWD = '密碼'

dict_of_element = {
    'URL': "https://healthy.mediatek.com/nws/#!LoginView",
    'UID': '//*[@id="gwt-uid-3"]',  # '//input[@type="text"]'
    'PWD': '//*[@id="gwt-uid-5"]',  # '//input[@type="password"]'
    'SUB': '//*[@id="nws-109514"]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[9]/div',
}


driver = webdriver.Chrome()
driver.get(dict_of_element['URL'])
time.sleep(2)
driver.find_element_by_xpath(dict_of_element['UID']).send_keys(USER_UID)
time.sleep(1)
driver.find_element_by_xpath(dict_of_element['PWD']).send_keys(USER_PWD)
time.sleep(1)
driver.find_element_by_xpath(dict_of_element['SUB']).click()

time.sleep(5)
driver.quit()
