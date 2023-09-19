from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import subprocess
from selenium.common.exceptions import NoSuchElementException
import time
from chrome_cmd_services import driver
from trading_view_screener import trading__view__screener

def trading__view__signIn():
    driver.get("https://www.tradingview.com/accounts/signin/")
    time.sleep(3)

    try:
        # Find elements with the text "Get started"
        try:
            check_element = driver.find_element(By.XPATH,"//p[contains(text(), 'Sign in')]") 
            if check_element:
                print("not sign in trading view")
                google_sign_in_element = driver.find_element(By.NAME,"Google")
                google_sign_in_element.click()
                print("sign in by google complete") 
                # new__tab__switch()
                trading__view__screener()
                driver.refresh()
            else:
                print("might have already sign in")
                # new__tab__switch()
                trading__view__screener()
        except:
        # else:
            print("check sign in manually")
            # new__tab__switch()
            trading__view__screener()
        # for switch if neeed
        # driver.switch_to.default_content()

        # Check if any elements with the text "Get started" were found
        # if len(check_get_started_elements) > 0:
        # if check_get_started_elements:
            
            
        # else:
            
        #     print("Already sign in trading view")

    except NoSuchElementException:
        print('----its trading view sign in error----')

