import os
from time import sleep
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

#TODO authorize

def driver_main():
    ''' 
    Main settings for webdriver session.
    ''' 
    op = Options()
    op.add_argument('-headless')
    driver = Firefox(executable_path=find_geckodriver(),firefox_options = op)
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
    Launchs test and save test.png in CWD.
    '''
    driver = driver_main()
    #cookie = {'name': 'token','value': 'Token5c30fe25e1737b62e9738b7463b8dedd32e9ba6a'}
    #driver.add_cookie(cookie)
    url = 'https://my.5ka.ru'
    driver.get(url)
    user_info = {'phone':'9377789729','phone_password':'s1stemofadown'}
    for k,v in user_info.items():
        text_input(k,v,driver)
    driver.find_element_by_xpath('//button[text()="Войти"]').click()
    sleep(1)
    sms_code = input('Enter 4 numbers from SMS: ')
    text_input('code',sms_code, driver)
    sleep(1)
    driver.save_screenshot('test.png')
    token = driver.get_cookie('token')
    print(token)

if __name__ == '__main__':
    driver_init()
