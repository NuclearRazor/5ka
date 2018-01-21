#! coding:utf-8
import json
import os
import pickle
import re
from time import sleep
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

def driver_main():
    ''' 
    Main settings for webdriver session.
    ''' 
    op = Options()
    op.add_argument('-headless')
    driver = Firefox(executable_path=find_geckodriver(),
                     firefox_options = op)
    driver.set_window_size(1024,768)
    return driver

def find_geckodriver():
    '''
    Finds geckodriver in executable paths. Looks in $PATH.
    '''
    exec_path = os.get_exec_path()
    for path in exec_path:
        queue = list(os.walk(path))
        if 'geckodriver' in queue[0][2]:
            return os.path.join(queue[0][0],'geckodriver')

def text_input(field,string,driver):
    ''' 
    Input <string> in to the <field>.
    ''' 
    element = driver.find_element_by_name(field)
    element.send_keys(string)

def driver_init():
    '''
    Test.
    '''
    driver = driver_main()
    url = 'https://my.5ka.ru/login'
    driver.set_window_size(1024, 768)
    driver.get(url)
    sleep(1)
    data = {'phone':'9377789729','phone_password':'s1stemofadown'}
    for k,v in data.items():
        text_input(k,v,driver)
    driver.find_element_by_xpath('//button[text()="Войти"]').click()
    sleep(1)
    sms_code = input('Enter SMS code: ')
    text_input('code',sms_code,driver)
    cookies = driver.get_cookies()
    driver.quit()
    return cookies

def request_json(cookies):
    token = cookies[1]['value']
    header = {'Host':'my.5ka.ru',
              'Accept': 'application/json, text/plain, */*',
              'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0',
              'X-Authorization':token
    }
    url = 'https://my.5ka.ru/api/v2/transactions/?card=07302bd9-c662-42f5-a10a-386fde0c8742&limit=100&offset=0&type='
    r = requests.get(url,headers=header)
    return r.text

if __name__ == '__main__':
    if os.path.isfile('cookies'):
        print('OK')
        with open('cookies','rb') as f:
            cookies = pickle.load(f)
        #print(cookies)
    else:
        cookies = driver_init()
        with open('cookies','wb') as f:
            pickle.dump(cookies,f)
        #print(cookies)
        print('Dumped!')
    json_data = request_json(cookies)
    print(json_data)
