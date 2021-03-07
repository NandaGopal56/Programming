from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
# Step 1) Open Firefox
browser=webdriver.firefox()
time.sleep(10)
# Step 2) Navigate to Facebook
browser.get("http://www.facebook.com")
# Step 3) Search & Enter the Email or Phone field & Enter Password
username = browser.find_element_by_id("email")
password = browser.find_element_by_id("pass")
submit = browser.find_element_by_id("loginbutton")
username.send_keys("nandagopalpattanayak@gmail.com")
password.send_keys("Nanda98k$gopal")
# Step 4) Click Login
submit.click()