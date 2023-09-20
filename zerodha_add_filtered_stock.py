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
from zerodha_buy_orders import zerodha__buy__orders
from zerodha_sell_positions import zerodha__sell__positions




def zerodha__add__filtered__stock(top_three_stocks):
    try:
        time.sleep(5)
        print('from zerodha_add_filter:',top_three_stocks)

        search_input_element = driver.find_element(By.CSS_SELECTOR, '.su-input-group input[type="text"]')

        for stock in top_three_stocks:
            # Extract the symbol from the list (without 'NSE:')
            symbol = stock['Symbol'].replace('NSE:', '')

            # Clear the search input field
            search_input_element.clear()

            # Enter the symbol into the search input field
            search_input_element.send_keys(symbol)

            # Press Enter to perform the search (you can uncomment this line if needed)
            # search_input_element.send_keys(Keys.RETURN)

            # Locate the "NSE" element (modify the selector if needed)
            nse_element = driver.find_element(By.XPATH, '//li[@class="search-result-item selected"]//span[@class="exchange-tag text-label text-label-outline NSE"]')

            # Create an ActionChains object to perform hover action
            actions = ActionChains(driver)

            # Perform a hover action on the "NSE" element
            actions.move_to_element(nse_element).perform()

            # Find and click the "Add" button (modify the selector if needed)
            add_button_element = driver.find_element(By.XPATH, '//button[@data-balloon="Add"]')
            add_button_element.click()

            
            body_element = driver.find_element(By.XPATH, '//body')
            body_element.click()


            zerodha__buy__orders()


# --------------------------SELL-------------------------------------
        
        # zerodha__sell__positions()


        

    

    except NoSuchElementException:
        # Switch back to the original window
        print('----zerodha add filter stocks in NoSuchElementException----')