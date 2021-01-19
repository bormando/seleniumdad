from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time


browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("http://the-internet.herokuapp.com/drag_and_drop")
action_chains = ActionChains(browser)
source = browser.find_element_by_css_selector("#column-a")
target = browser.find_element_by_css_selector("#column-b")
action_chains.drag_and_drop(source, target).perform()
time.sleep(3)
browser.close()
