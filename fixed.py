from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("http://the-internet.herokuapp.com/drag_and_drop")
source = browser.find_element_by_css_selector("#column-a")
target = browser.find_element_by_css_selector("#column-b")
f = open("script.js",  "r")
javascript = f.read()
f.close()
time.sleep(3)
browser.execute_script(javascript, source, target)
time.sleep(3)
browser.close()
