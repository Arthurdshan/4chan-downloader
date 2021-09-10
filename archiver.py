from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

def get_screenshot(url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    driver.get(url)
    
    elem = lambda x: driver.execute_script('return document.body.parentNode.scroll' + x)
    
    driver.set_window_size(1920, elem('Height') + 1000)
    name = input('\nType the name of the file: ').strip() + ".png"
    driver.find_element_by_tag_name('body').screenshot(name)
    driver.close()
    sleep(2)
    print('Done')