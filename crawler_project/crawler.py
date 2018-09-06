from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time, sys

# Command line arguments for email and password
user_email = sys.argv[1]
user_password = sys.argv[2]

# Sets up Chrome as browser as it is on local machine
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.maximize_window() # optional

# Website to visit
driver.get('https://facebook.com/')

# Fills user email
email_input = driver.find_element_by_id('email')
email_input.send_keys(user_email)

# Fills user password
password_input = driver.find_element_by_id('pass')
password_input.send_keys(user_password)

# Finds and clicks login button
login_btn = driver.find_element_by_id('loginbutton')
login_btn.click()

# Finds the tag to visit user profile
profile_link = driver.find_element_by_class_name('_1k67')
profile_link.click()

# Creates url to view friends page
current_url = driver.current_url
friends_url = current_url + '/friends'

driver.get(friends_url)

friend_list = driver.find_element_by_class_name('uiList')

html = driver.page_source
soup = BeautifulSoup(html, 'lxml')
for tag in soup.find_all('li'):
	anchor = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, "a")))
	anchor.click()





















