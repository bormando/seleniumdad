from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time


browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.seleniumeasy.com/test/drag-and-drop-demo.html")
action_chains = ActionChains(browser)
source = browser.find_element_by_css_selector("span[draggable]:nth-child(2)")
target = browser.find_element_by_css_selector("#mydropzone")
action_chains.drag_and_drop(source, target).perform()
time.sleep(3)
browser.close()
