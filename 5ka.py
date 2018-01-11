import os
import requests
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait as wdw

#TODO authorize

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
    url = 'https://my.5ka.ru/login'
    op = Options()
    op.add_argument('-headless')
    findd = find_geckodriver()
    driver = Firefox(executable_path=findd,firefox_options = op)
    driver.get(url)
    wait = wdw(driver,1)
    driver.save_screenshot('test.png')
    driver.quit()

if __name__ == '__main__':
    driver_init()
