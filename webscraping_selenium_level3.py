from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# optional argument for Chrome Driver - ensure Chrome is configured for full screen
options = webdriver.ChromeOptions()
options.add_argument("--start-fullscreen")
driver = webdriver.Chrome(chrome_options=options)

# navigate to the right webpage
driver.get('https://www.coles.com.au')

# find the search box and enter my keyword
search_bar = driver.find_element_by_id("ctl19_ctl02_txtSearch")
search_bar.send_keys("Free Range Chicken Stir Fry")

# optional - pause for 4s
time.sleep(4)

# click search to find my item
search_icon = driver.find_element_by_id("ctl19_ctl02_btnButtonSearch")
search_icon.click()

# optional - pause for 4s
time.sleep(4)

# optional - to scroll down and view my item
driver.execute_script("window.scrollBy(0, 600);")

# extract the price for my item
price = driver.find_element_by_css_selector(".product-price").text

# optional - pause for 4s
time.sleep(4)

print("Free Range Chicken Stir Fry From Coles = {price}".format(price=price))

# optional - pause for 4s
time.sleep(4)
driver.close()
