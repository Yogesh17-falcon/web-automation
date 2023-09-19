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
from zerodha_add_filtered_stock import zerodha__add__filtered__stock



def zerodha__access__filter__value(top_three_stocks):
    try:
        time.sleep(3)
        # understand button click
        upderstandElem = driver.find_element(By.XPATH, "//button[contains(text(), 'I understand')]")
        time.sleep(2)
        upderstandElem.click()   

        print('from zerodha dashboard')

        # access stocks from select_value_from filter
        print('from zerodha_access_filter:',top_three_stocks)
        # for stock in top_three_stocks:
        #     print(f"Symbol: {stock['Symbol']}, Close Price: {stock['Close Price']}")
        
        zerodha__add__filtered__stock(top_three_stocks)



    except NoSuchElementException:
        # Switch back to the original window
        print('----zerodha access value from filter in NoSuchElementException----')