# 31/07/2024
# Day - 049



##################################################
# DAY 49 PROJECT: LINKEDIN SAVE JOBS

print("\n*** Welcome to the Automated LinkedIn Bot: SOLUTION (TWEAKED)***")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import os


ACCOUNT_EMAIL = os.environ.get("EMAIL")
ACCOUNT_PASSWORD = os.environ.get("PW")
PHONE = os.environ.get("PHONE")

print(ACCOUNT_EMAIL, ACCOUNT_PASSWORD, PHONE)



url = "https://www.linkedin.com/jobs/search?keywords=Python%20Developer&location=Espa%C3%B1a&geoId=105646813&f_JT=F&f_TPR=&f_WT=2&f_E=2%2C4&position=1&pageNum=0"

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)


# Click Sign in Button
time.sleep(4)
sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Inicia sesión")
sign_in_button.click()

# Sign in
time.sleep(5)
email_field = driver.find_element(by=By.ID, value="username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

# You may be presented with a CAPTCHA - Solve the Puzzle Manually
input("Press Enter when you have solved the Captcha")



# Solicitud sencilla: Locate the apply button: 
try:
    # Esperar hasta que el botón sea visible
    button_apply = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".jobs-apply-button"))
    )
    button_apply.click()
except Exception as e:
    print(f"Error: {e}")


#If application requires phone number and the field is empty, then fill in the number.
time.sleep(5)
phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
if phone.text == "":
    phone.send_keys(PHONE)

# #Submit the application
# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
# submit_button.click()

# TBC