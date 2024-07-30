# 24/07/2024
# Day - 048



##################################################
# DAY 48 PROJECT: COOKIES

print("\n*** Welcome to: Become the Cookie Master! ***")

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


url = "http://orteil.dashnet.org/experiments/cookie/"

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)



print("\nFind Element By ID:")

def get_elements():
    buy_elements = {
        "buyCursor": driver.find_element(By.ID, value="buyCursor"),
        "buyGrandma": driver.find_element(By.ID, value="buyGrandma"),
        "buyFactory": driver.find_element(By.ID, value="buyFactory"),
        "buyMine": driver.find_element(By.ID, value="buyMine"),
        "buyShipment": driver.find_element(By.ID, value="buyShipment"),
        "buyAlchemy": driver.find_element(By.ID, value="buyAlchemy lab"),
        "buyPortal": driver.find_element(By.ID, value="buyPortal"),
        "buyTime": driver.find_element(By.ID, value="buyTime machine")
    }
    return buy_elements


cookie = driver.find_element(By.ID, value="cookie")
buy_elements = get_elements()

# Create the array of elements from most expensive to least expensive
elements = [
    buy_elements["buyTime"],
    buy_elements["buyPortal"],
    buy_elements["buyAlchemy"],
    buy_elements["buyShipment"],
    buy_elements["buyMine"],
    buy_elements["buyFactory"],
    buy_elements["buyGrandma"],
    buy_elements["buyCursor"]
]

timeout = time.time() + 5
five_min = time.time() + 60*5  # 5 minutes


while True:
    
    cookie.click()
    
    if time.time() > timeout:
        buy_elements = get_elements()
        
        elements = [
            buy_elements["buyTime"],
            buy_elements["buyPortal"],
            buy_elements["buyAlchemy"],
            buy_elements["buyShipment"],
            buy_elements["buyMine"],
            buy_elements["buyFactory"],
            buy_elements["buyGrandma"],
            buy_elements["buyCursor"]
        ]
        
        for element in elements:
            try:
               element.click()
            except Exception as e:
               print(f"Could not click {element}: {e}")
               
        # Add another 5 seconds until the next check
        timeout = time.time() + 5