# 24/07/2024
# Day - 048



##################################################
print("\n\n*** Selenium ***")

from selenium import webdriver
from selenium.webdriver.common.by import By



# Can't use the live version: antibot policy
url = "https://appbrewery.github.io/instant_pot/"
# url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text

print(f"The price is {price_dollar}.{price_cents}")


# Close a single tab, the active tab where you have opened a particular page:
# driver.close()
# Quit the entire browser:
# driver.quit()