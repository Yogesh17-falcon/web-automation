from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import subprocess
from selenium.common.exceptions import NoSuchElementException
import time
from chrome_cmd_services import driver
from trading_view_filter import trading__view__filter


def trading__view__screener():
    driver.get("https://in.tradingview.com/screener/")
    time.sleep(5)
    try:
        print("Screener")
        trading__view__filter()
        time.sleep(3)
        
       
        

            
    # trading__view__filter()

    except NoSuchElementException:
        print('----trading view screener error----')

