from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import subprocess
from selenium.common.exceptions import NoSuchElementException
import time
from chrome_cmd_services import driver
import os
from dotenv import load_dotenv
from zerodha_access_filter_value import zerodha__access__filter__value

# Load environment variables from .env file
load_dotenv()

# Retrieve email and password from environment variables
zUserId = os.getenv("ZUSERID")
zPassword = os.getenv("ZPASSWORD")

def zerodha__log__in(top_three_stocks):
    try:
        driver.get("https://kite.zerodha.com/dashboard")

        try:
            check_element = driver.find_element(By.XPATH,"//h2[contains(text(), 'Login to Kite')]") 
            if check_element:
                print("not sign in zerodha or first time log in needs to enter both user id and password")
                zUserIdElem = driver.find_element(By.ID,"userid") 
                zUserIdElem.send_keys(zUserId)
                zUserIdElem.send_keys(Keys.RETURN)  
                time.sleep(3)

                zPassElem = driver.find_element(By.ID,"password") 
                zPassElem.send_keys(zPassword)
                zPassElem.send_keys(Keys.RETURN)  
                time.sleep(3)

                #needs to enter TOPTP
                time.sleep(5)
                print("sign in by zerodha will complete - enter totp manually") 
                # new__tab__switch()
                # driver.refresh()
            else:
                print("check zerodha sign (userid, password) in manually")

                # new__tab__switch()
        except:
        # else:
            print("only need password and totp for second time")
            zPassElem = driver.find_element(By.ID,"password") 
            zPassElem.send_keys(zPassword)
            zPassElem.send_keys(Keys.RETURN)  
            time.sleep(7)
            print("sign in by zerodha will complete - enter totp manually") 
            print("check zerodha sign (password) in manually")
            # new__tab__switch()


            

            # open dashboard & acess value from filter
            zerodha__access__filter__value(top_three_stocks)



    except NoSuchElementException:
        # Switch back to the original window
        print('----zerodha log in NoSuchElementException----')