# 24/07/2024
# Day - 048



##################################################
print("\n\n*** Selenium: Wikipedia ***")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



url = "https://en.wikipedia.org/wiki/Main_Page"

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)


print("\nFind Element By XPATH:")
# https://www.w3schools.com/xml/xpath_intro.asp
n_articles = driver.find_element(By.XPATH, value="/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[1]/div/div[3]/a[1]")
print(n_articles)

print("\nFind Element By CSS_SELETOR:")
article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(article_count.text)

print("\nClicking on the Article Count:")
# article_count.click()

print("\nFind Element By LINK_TEXT:")
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

print("\nFind Element By NAME: search_bar")
search_bar = driver.find_element(By.NAME, value="search")
search_bar.send_keys("Python", Keys.ENTER)


# Close a single tab, the active tab where you have opened a particular page:
# driver.close()
# Quit the entire browser:
# driver.quit()