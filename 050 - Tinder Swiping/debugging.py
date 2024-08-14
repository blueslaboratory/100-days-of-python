# 13/08/2024

# 1º CMD:
# "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\Users\AlejandroDiezRedondo\AppData\Local\Google\Chrome\User Data"

# 2º:
# > pip install webdriver-manager

# 3º:
# Run the program



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

# Automatically downloads the correct ChromeDriver and uses it
driver = webdriver.Chrome(service=webdriver.chrome.service.Service(ChromeDriverManager().install()), options=options)

# Now you can control the already opened Chrome window
# driver.get("https://www.tinder.com")



# Wait until the profile card is present and click the like button
print("\n*** HACER 1 SWIPE RIGHT! ***")

input("Press Enter to swipe right")

try:
    print("Find Element By XPATH:")
    button_like = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Like']]"))   
    )
    
    button_like.click()
    
except Exception as e:
    print(f"An error occurred: {e}")
    
print("\n*** Alright! Llegamos al final! ***")