# 24/07/2024
# Day - 048



##################################################
print("\n\n*** Selenium ***")

from selenium import webdriver
from selenium.webdriver.common.by import By



url = "https://www.python.org/"

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

print("\nFind Element By NAME: search_bar")
search_bar = driver.find_element(By.NAME, value="q")

print("\nSearch Bar:")
print(search_bar)

print("\nSearch Bar: tag_name")
print(search_bar.tag_name)

print("\nSearch Bar: get_attribute")
print(search_bar.get_attribute("placeholder"))

print("\nFind Element By ID:")
button = driver.find_element(By.ID, value="submit")
print(button.size)

print("\nFind Element By CSS_SELETOR:")
documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

print("\nFind Element By XPATH:")
# https://www.w3schools.com/xml/xpath_intro.asp
bug_link = driver.find_element(By.XPATH, value="/html/body/div/footer/div[2]/div/ul/li[3]/a")
print(bug_link.text)


print("\nFind Multiple Elements By XPATH:")

upcoming_events = {}

for i in range(5):
    time = driver.find_element(By.XPATH, value=f"/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li[{i+1}]/time")
    name = driver.find_element(By.XPATH, value=f"/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li[{i+1}]/a")
    
    upcoming_events[i] = {
        "time":time.text, 
        "name":name.text
    }
    
print(upcoming_events)
    

print("\nFind Multiple Elements By CCSS_SELECTOR:")
event_times = driver.find_elements(By.CSS_SELECTOR, value=f".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=f".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }

print(events)


# Close a single tab, the active tab where you have opened a particular page:
# driver.close()
# Quit the entire browser:
# driver.quit()