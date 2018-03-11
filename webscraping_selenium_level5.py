from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# optional argument for Chrome Driver - ensure Chrome is configured for full screen
options = webdriver.ChromeOptions()

# Headless Chrome example
options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=options)

timeout = 4
wait = WebDriverWait(driver, timeout)

driver.get('https://www.coles.com.au')

# find the search box and enter my keyword
search_bar = wait.until(EC.presence_of_element_located((By.ID, 'ctl19_ctl02_txtSearch')))
search_bar.send_keys("Free Range Chicken Stir Fry")

# click search to find my item
search_icon = wait.until(EC.presence_of_element_located((By.ID, 'ctl19_ctl02_btnButtonSearch')))
search_icon.click()

# extract the price for my item
target_price = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.product-price')))
price = target_price.text

print("Free Range Chicken Stir Fry From Coles = {price}".format(price=price))
driver.close()