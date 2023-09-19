from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import subprocess
from selenium.common.exceptions import NoSuchElementException
import time
from chrome_cmd_services import driver


def new__tab__switch():
    try:
        driver.switch_to.new_window('tab')
        # Switch to the new window
        driver.switch_to.window(driver.window_handles[1])

        # Open a URL in the new window
        # driver.get("https://in.tradingview.com")

    except NoSuchElementException:
        # Switch back to the original window
        driver.switch_to.window(driver.window_handles[0])
        print('----new window NoSuchElementException----')

