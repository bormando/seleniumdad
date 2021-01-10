from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.seleniumeasy.com/test/drag-and-drop-demo.html")
source = browser.find_element_by_css_selector("span[draggable]:nth-child(2)")
target = browser.find_element_by_css_selector("#mydropzone")
f = open("script.js",  "r")
javascript = f.read()
f.close()
time.sleep(3)
browser.execute_script(javascript, source, target)
time.sleep(3)
browser.close()
