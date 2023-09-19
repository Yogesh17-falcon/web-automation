from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import subprocess
import time
import os
from dotenv import load_dotenv
from selenium.common.exceptions import NoSuchElementException
from chrome_cmd_services import driver
from swith_new_tab import new__tab__switch
from trading_view_sigIn import trading__view__signIn

# def google__sign__function(name):
#   print("Hello, " + name)

load_dotenv()
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")


def google__sign__function():
  driver.get("https://accounts.google.com")
  time.sleep(3)

  try:
      # Already signed in
      check_element = driver.find_element(By.XPATH,"//h1[contains(text(), 'Welcome')]") 
      print("Already! signed in google.")

      #after sign in switch to the new tab
      new__tab__switch()

      # can specify my trading view screener here
      # driver.get("https://in.tradingview.com/screener/")
      trading__view__signIn()

  except NoSuchElementException:
      # for check the sign and sign out but forgot to remove account
      try:
        check_element = driver.find_element(By.CLASS_NAME,"pQ0lne") 
        class_attr = check_element.get_attribute('class')
        class_names = class_attr.split(' ')
        
        specific_class_name = 'pQ0lne'

        if specific_class_name in class_names:
            print('already sign out! but doesnt remove account')
            select_sign_in_element = driver.find_element(By.XPATH,"//div[contains(text(), 'Yogesh')]")
            select_sign_in_element.click() 
            time.sleep(5)
            password_element = driver.find_element(By.NAME,"password")
            password_element.send_keys(password) 
            password_element.send_keys(Keys.RETURN) 
        else:
            print('The element does not have specified class name.')
            exit
          
      except NoSuchElementException:
        # Sign in for completely new and removed account
        # Find the email input field and enter your email/username
        email_element = driver.find_element(By.NAME,"identifier") 
        email_element.send_keys(email)
        email_element.send_keys(Keys.RETURN)  

        # Wait for a while to allow the page to load
        time.sleep(5)

        # Find the password input field and enter your password
        password_element = driver.find_element(By.NAME,"Passwd") 
        password_element.send_keys(password) 
        password_element.send_keys(Keys.RETURN)  

        # Wait for a while to allow the login process to complete
        time.sleep(5)
        print("Signed In Complete.")


