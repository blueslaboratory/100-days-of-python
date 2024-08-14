# 08/08/2024
# Day - 050



##################################################
# DAY 50 PROJECT: TINDER BOT

print("\n*** Welcome to the Tinder Bot! ***")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import time



URL = "https://tinder.com/"

PHONE = os.environ.get("PHONE")
print(PHONE)



# Keep firefox browser open after program finishes
# firefox_options = webdriver.FirefoxOptions()
# firefox_options.add_argument("--start-maximized")
# firefox_options.add_argument("--private")

# driver = webdriver.Firefox(options=firefox_options)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--incognito")
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)



driver.get(URL)

# Esperar a que el elemento esté presente
driver.implicitly_wait(5)



print("\n*** INICIAR SESION ***")

print("Find Element By LINK_TEXT:")
button_login1 = driver.find_element(By.LINK_TEXT, value="Inicia sesión")
button_login1.click()

# Esperar a que el elemento esté presente
driver.implicitly_wait(10)

print("Find Element By XPATH:")
# https://www.w3schools.com/xml/xpath_intro.asp
button_login2 = driver.find_element(By.XPATH, "//*[contains(@class, 'Mend(a)') and contains(text(), 'Iniciar sesión con nº de teléfono')]")
button_login2.click()

# Esperar a que el elemento esté presente
driver.implicitly_wait(10)



print("\n*** PHONE CODE ***")

print("Find Element By CSS_SELECTOR:")
country_input = driver.find_element(By.CSS_SELECTOR, value="input")
country_input.send_keys(PHONE)

# Esperar a que el elemento esté presente
driver.implicitly_wait(10)

print("Find Element By XPATH:")
button_next = driver.find_element(By.XPATH, "//*[contains(@class, 'lxn9zzn') and contains(text(), 'Siguiente')]")
button_next.click()

# Esperar a que el elemento esté presente
driver.implicitly_wait(10)



print("\n*** IFRAMES ***")

# Esperar hasta que el primer iframe esté presente y cambiar a él
print("Find Element By XPATH:")
iframe1 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src, 'tinder-api.arkoselabs.com')]"))
)
driver.switch_to.frame(iframe1)

# Esperar a que el segundo iframe esté presente y cambiar a él
print("Find Element By ID:")
iframe2 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "fc-iframe-wrap"))
)
driver.switch_to.frame(iframe2)

# Esperar a que el tercer iframe esté presente y cambiar a él
print("Find Element By ID:")
iframe3 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "CaptchaFrame"))
)
driver.switch_to.frame(iframe3)

print("Find Element By ID:")
button_verify = driver.find_element(By.ID, value="home_children_button")
button_verify.click()

# Volver al contenido principal después de la interacción
driver.switch_to.default_content()



print("\n*** CAPTCHA - Solve the Puzzle Manually ***")

input("Press Enter when you have solved the Captcha and entered the code: ")

print("Find Element By XPATH:")
button_next = driver.find_element(By.XPATH, "//*[contains(@class, 'lxn9zzn') and contains(text(), 'Siguiente')]")
button_next.click()



print("\n*** CODIGO CORREO ***")

print("Find Element By XPATH:")
button_next = driver.find_element(By.XPATH, "//*[contains(@class, 'lxn9zzn') and contains(text(), 'Enviar correo')]")
button_next.click()

input("Press Enter when you have entered the code: ")

print("Find Element By XPATH:")
button_next = driver.find_element(By.XPATH, "//*[contains(@class, 'lxn9zzn') and contains(text(), 'Siguiente')]")
button_next.click()



print("\n*** PERMITIR LOCALIZACION ***")

print("Find Element By XPATH:")
button_next = driver.find_element(By.XPATH, "//*[contains(@class, 'lxn9zzn') and contains(text(), 'Permitir')]")
button_next.click()



print("\n*** DESACTIVAR NOTIFICACIONES ***")

print("Find Element By XPATH:")
button_next = driver.find_element(By.XPATH, "//*[contains(@class, 'lxn9zzn') and contains(text(), 'Creo que paso')]")
button_next.click()




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