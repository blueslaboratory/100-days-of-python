# 24/07/2024
# Day - 048



##################################################
print("\n\n*** Selenium: Sign Up ***")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



url = "https://secure-retreat-92358.herokuapp.com/"

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)



print("\nFind Element By LINK_TEXT:")

input_fname = driver.find_element(By.NAME, value="fName")
input_fname.send_keys("Blue's")

input_lname = driver.find_element(By.NAME, value="lName")
input_lname.send_keys("Laboratory")

input_email = driver.find_element(By.NAME, value="email")
input_email.send_keys("blueslaboratory@lab.com")

print("\nFind Element By LINK_TEXT:")
sign_up = driver.find_element(By.CSS_SELECTOR, value=".btn")
sign_up.click()



# Close a single tab, the active tab where you have opened a particular page:
# driver.close()
# Quit the entire browser:
# driver.quit()