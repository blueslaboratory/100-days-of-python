# 04/10/2024
# Day - 051



##################################################
# DAY 51 PROJECT: XBOT SOLUTION

print("\n*** Welcome to the X Bot! ***")


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import os


PROMISED_DOWN = 300
PROMISED_UP = 300
TWITTER_USER = os.environ.get("USER")
TWITTER_PASSWORD = os.environ.get("PW")


class InternetSpeedXBot:
    
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--incognito")
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=chrome_options)
        # self.driver = webdriver.Chrome()
        
        self.up = 100
        self.down = 100



    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        # Depending on your location, you might need to accept the GDPR pop-up.
        # accept_button = self.driver.find_element(By.ID, value="_evidon-banner-acceptbutton")
        # accept_button.click()

        time.sleep(5)

        go_button = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a")
        go_button.click()

        time.sleep(55)
        self.down = float(self.driver.find_element(By.CLASS_NAME, "download-speed").text)
        self.up = float(self.driver.find_element(By.CLASS_NAME, "upload-speed").text)



    def tweet_at_provider(self):
        self.driver.get("https://x.com/login")
        
        '''
        # Hacerlo con un sleep:
        time.sleep(5)
        login_user = self.driver.find_element(By.CSS_SELECTOR, value="input")
        '''
        
        # Hacerlo con EC:
        # Espera a que el campo de usuario este visible
        login_user = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input"))
        )
        # Espera a que el campo de usuario este presente
        login_user = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input"))
        )
        

        login_user.send_keys(TWITTER_USER)
        login_user.send_keys(Keys.ENTER)
        
        '''
        # Hacerlo con un sleep:
        time.sleep(5)
        login_pw = self.driver.find_element(By.CSS_SELECTOR, value="input[type='password']")
        '''

        # Hacerlo con EC:
        # Espera a que el campo de contraseña este presente
        login_pw = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password']"))
        )
        
        
        login_pw.send_keys(TWITTER_PASSWORD)
        login_pw.send_keys(Keys.ENTER)
        # time.sleep(5)
        
        
        if (self.down < 300 or self.up < 300):
            
            tweet = f"Hey Internet Provider, why is my internet speed {self.down}Mbps down/{self.up}Mbps up when I pay for {PROMISED_DOWN}Mbps down/{PROMISED_UP}Mbps up?"
            


            '''
            # Hacerlo con un sleep:
            tweet_compose = self.driver.find_element(By.XPATH, '//div[@data-testid="tweetTextarea_0"]')
            tweet_compose.click()
            tweet_compose.send_keys(tweet)
            time.sleep(3)
            '''

            # Hacerlo con EC:
            # Espera a que el elemento este visible
            tweet_compose = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//div[@data-testid="tweetTextarea_0"]'))
            )            
            print("Element located, clicking now...")

            # Click on the tweet text area to focus
            tweet_compose.click()
            tweet_compose.send_keys(tweet)

            

            '''
            # Hacerlo con un sleep:
            tweet_button = self.driver.find_element(By.XPATH, value='??')
            tweet_button.click()
            time.sleep(3)
            '''

            # Hacerlo con EC:
            tweet_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="tweetButtonInline"]'))
            )
            print("Tweet button located, attempting to click...")

            # Click on the button to focus
            tweet_button.click()
            
            
            
            # self.driver.quit()



bot = InternetSpeedXBot()



print("\nGet Internet Speed:")
bot.get_internet_speed()

print(f"Download Speed: {bot.down}Mbps")
print(f"Upload Speed: {bot.up}Mbps")



print("\nTweet at provider:")
bot.tweet_at_provider()