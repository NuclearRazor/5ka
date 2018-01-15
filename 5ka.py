#! coding:utf-8
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait as WDC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#TODO check login or card page.

def driver_main():
    ''' 
    Main settings for webdriver session.
    ''' 
    fp = webdriver.FirefoxProfile('/home/goosique/.mozilla/firefox/yhn2ttuv.default')
    op = Options()
    op.add_argument('-headless')
    driver = Firefox(firefox_profile=fp,
                     executable_path=find_geckodriver(),
                     firefox_options = op)
    driver.set_window_size(1024,768)
    return driver

def text_input(field,string,driver):
    ''' 
    Input <string> in to the <field>.
    ''' 
    element = driver.find_element_by_name(field)
    element.send_keys(string)

def find_geckodriver():
    '''
    Finds geckodriver in executable paths. Looks in $PATH.
    '''
    exec_path = os.get_exec_path()
    for path in exec_path:
        queue = list(os.walk(path))
        if 'geckodriver' in queue[0][2]:
            return os.path.join(queue[0][0],'geckodriver')

def driver_init():
    '''
    Test.
    '''
    driver = driver_main()
    url = 'https://my.5ka.ru'
    driver.get(url)
    #sleep(1)
    wait = WDC(driver,5)
    try:
        check = wait.until(EC.presence_of_element_located((By.NAME,'phone')))
        driver.save_screenshot('test.png')
        user_info = {'phone':'9377789729','phone_password':'s1stemofadown'}
        for k,v in user_info.items():
            text_input(k,v,driver)
        driver.find_element_by_xpath('//button[text()="Войти"]').click()
        sleep(1)
        sms_code = input('Enter 4 numbers from SMS: ')
        text_input('code',sms_code, driver)
    except:
        driver.save_screenshot('test_p.png')
    #token = driver.get_cookie('token')
    #print(token)
    finally:
        driver.quit()

if __name__ == '__main__':
    driver_init()
