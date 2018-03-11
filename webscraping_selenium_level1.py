import time
from selenium import webdriver

# optional argument, you can add specific path to find your webdriver
# link - https://sites.google.com/a/chromium.org/chromedriver/getting-started

driver = webdriver.Chrome()
driver.get('http://www.google.com/xhtml')

# optional - pause for 4s
time.sleep(4)

# find the name of the element called q and enter 'ChromeDriver' into the textbox
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()

# # optional - pause for 4s
time.sleep(4)
driver.quit()
