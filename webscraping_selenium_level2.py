import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# optional argument for Chrome Driver - ensure Chrome is configured for full screen
options = webdriver.ChromeOptions()
options.add_argument("--start-fullscreen")
driver = webdriver.Chrome(chrome_options=options)

# navigate to the right webpage
driver.get('https://www.yourmortgage.com.au/calculators/')

# asking for the loan amount and interest amount
loan_amount = input("Loan Amount ? > ")
interest_amount = input("Interest Amount ? > ")

# optional - pause for 4s
time.sleep(4)

# find the ID element called LoanAmount and enter the loan amount into the textbox
loan = driver.find_element_by_id('LoanAmount')
loan.send_keys(loan_amount)

# find the ID element called InterestRate and enter the interest amount into the textbox
interest = driver.find_element_by_id('InterestRate')

# optional - pause for 4s
time.sleep(4)

# why do we need to use BACK_SPACE 3 times ? - play with it!
interest.send_keys(Keys.BACK_SPACE)
interest.send_keys(Keys.BACK_SPACE)
interest.send_keys(Keys.BACK_SPACE)
interest.send_keys(interest_amount)

# find the css element and click the search button
calculate = driver.find_element_by_css_selector('.form-group-btn [type]')
calculate.click()

# extract all the data we needed
monthly = driver.find_element_by_id('repayment3').text
total_loan = driver.find_element_by_id('totalRepayment1').text
total_interest = driver.find_element_by_id('totalInterest2').text

print("Monthly repayment = {monthly}".format(monthly=monthly))
print("Total loan repayments = {total_loan}".format(total_loan=total_loan))
print("Total interest paid = {total_interest}".format(total_interest=total_interest))

# optional - pause for 5s
time.sleep(4)
driver.quit()
