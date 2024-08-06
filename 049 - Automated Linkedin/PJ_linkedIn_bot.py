# 31/07/2024
# Day - 049



##################################################
# DAY 49 PROJECT: LINKEDIN SAVE JOBS

print("\n*** Welcome to the Automated LinkedIn Bot ***")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException

import os
import time


url = "https://www.linkedin.com/jobs/search?keywords=Python%20Developer&location=Espa%C3%B1a&geoId=105646813&f_JT=F&f_TPR=&f_WT=2&f_E=2%2C4&position=1&pageNum=0"

linkedin_email = os.environ.get("EMAIL")
linkedin_pw = os.environ.get("PW")

print(linkedin_email, linkedin_pw)


# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)



# Esperar a que el elemento esté presente
driver.implicitly_wait(4)

# Iniciar sesion
print("\nFind Element By LINK_TEXT:")
hyperlink_sign_in = driver.find_element(By.LINK_TEXT, value="Inicia sesión")
hyperlink_sign_in.click()


# Rellenar el formulario
print("\nFind Element By ID:")
input_email = driver.find_element(By.ID, value="username")
input_email.send_keys(linkedin_email)

input_pw = driver.find_element(By.ID, value="password")
input_pw.send_keys(linkedin_pw)



# Iniciar sesion
# Esperar a que el elemento esté presente
driver.implicitly_wait(2)

print("\nFind Element By CSS_SELECTOR:")
button_sign_in = driver.find_element(By.CSS_SELECTOR, value=".login__form_action_container button")
button_sign_in.click()



# You may be presented with a CAPTCHA - Solve the Puzzle Manually
input("Press Enter when you have solved the Captcha")



# Locate the save button
# try:
#     # Esperar hasta que el botón sea visible
#     button_save = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.CSS_SELECTOR, ".jobs-save-button"))
#     )
#     button_save.click()
# except Exception as e:
#     print(f"Error: {e}")



# Solicitud sencilla: Locate the apply button: 
# try:
#     # Esperar hasta que el botón sea visible
#     button_apply = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.CSS_SELECTOR, ".jobs-apply-button"))
#     )
#     button_apply.click()
# except Exception as e:
#     print(f"Error: {e}")




# Función para hacer scroll en un div específico
def scroll_in_div(driver, element):
    # driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", element)
    
    # Baja de 1/5 en 1/5, por eso hay un range(5) abajo, asi "carga" los elementos
    driver.execute_script("arguments[0].scrollTop += arguments[0].scrollHeight/5", element)
    time.sleep(3)  # Espera para que las nuevas ofertas se carguen



# Procesar todas las tarjetas de trabajo
try:
    # Encuentra el div que contiene las tarjetas de trabajo
    job_container_div = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".jobs-search-results-list"))
    )
    
    # Desplazar dentro del div para cargar más ofertas
    for i in range(5): 
        scroll_in_div(driver, job_container_div)


    job_cards = driver.find_elements(By.CSS_SELECTOR, ".job-card-container")
    print("Número de job cards encontrados:", len(job_cards))
    
    
    for index, job_card in enumerate(job_cards):
        
            try:
                job_card.click()
                time.sleep(3)  # Tiempo para hacer clic y abrir la oferta

                try:
                    # Esperar hasta que el botón "Guardar" sea visible
                    button_save = WebDriverWait(driver, 5).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, ".jobs-save-button span"))
                    )
                    
                    # Verifica el texto del botón para decidir si hacer clic
                    button_text = button_save.text.strip()
                    
                    if button_text != "Guardado":  # Ajusta el texto según el idioma y estado del botón
                        button_save.click()
                        
                        # Esperar brevemente para asegurar que la acción de guardar se complete
                        WebDriverWait(driver, 2).until(
                            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".jobs-save-button span"), "Guardado")
                        )
                        
                        print("Exito al guardar el trabajo - index:", index)
                    else:
                        print("El trabajo ya está guardado.")
                    
                except (NoSuchElementException, TimeoutException) as e:
                    print(f"Error al encontrar el botón de guardar: {e}")
            except Exception as e:
                print(f"Error al procesar la tarjeta de trabajo: {e}")

except Exception as e:
    print(f"An error occurred: {e}")
