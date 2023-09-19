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
from select_value_from_filter import select__value__from__filter
from sets_quantity_price import filter__id


def trading__view__filter():
    try:
        time.sleep(3)
        dropdownEle = driver.find_element(By.CSS_SELECTOR, '[data-name="screener-filter-sets"]')
        # time.sleep(5)
        dropdownEle.click() 
        # time.sleep(5)
        # # dropdownEle2 = driver.find_element(By.CSS_SELECTOR, '.tv-screener-popup__items-wrap') 
        # # Instead of volume leadres --> we can provide our filter name
        # text_filter = "Volume leaders"
        # time.sleep(5)
        # # dropdown_item = driver.find_element(By.XPATH, f'//div[contains(text(),"{text_filter}")]')

        # dropdown_item.click()


        # data-set="4486592" - S - TOP LOSERS
        # data-set="4437803" - B - TOP GAINERS
        # data-set="4437799" - B - VWAP CROSS SMA50
        # data-set="4175380" - S - VERY RISKY - INTRADAY
        # data-set="4175374" - B - VERY RISKY - INTRADAY
        # data-set="4175365" - B - UPTREND
        # data-set="4175361" - DIVIDEND STOCKS
        # data-set="4175349" - L B - BOUNCEPLAY - VERY RISKY
        # data-set="4175338" - S - HOLD - RISKY
        # data-set="4175325" - B - Breakouts Stocks
        # data-set="4175301" - L B - BOUNCEBACK (RISK HIGH)
        # data-set="4175281" - B - LONG TERM HOLD
        # data-set="4175264" - S - GAP DOWN STOCKS
        # data-set="4175244" - B - GAP UP STOCKS
        # data-set="4175228" - B - 50 MA CROSS ABV 200MA
        # data-set="4174707" - B - INTRADAY - (- ve 3)

        # id_element = 4174707
        id_element = filter__id


        scroll_element = driver.find_element(By.CSS_SELECTOR, f'div[data-set="{id_element}"]')
        driver.execute_script("arguments[0].scrollIntoView();", scroll_element)

        time.sleep(3)

        dropdown_item_element = driver.find_element(By.CSS_SELECTOR, f'div[data-set="{id_element}"]')
        dropdown_item_element.click()

        # store value from filter
        select__value__from__filter()

    except NoSuchElementException:
        # Switch back to the original window
        print('----trading view filter NoSuchElementException----')