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
from zerodha_logIn import zerodha__log__in
from sets_quantity_price import select__numbers__of__stocks


def select__value__from__filter():
    try:
        time.sleep(5)
        rows_element = driver.find_elements(By.CLASS_NAME, 'tv-data-table__row')


        # Initialize an empty list to store the top three stocks
        top_three_stocks = []

        # for all stocks
        # for row in rows_element:

        # for the top three stocks
        for row in rows_element[:select__numbers__of__stocks]:
       
            stock_info = {}
            cells = row.find_elements(By.CLASS_NAME, 'tv-data-table__cell')

            stock_info['Symbol'] = row.get_attribute('data-symbol')
            # stock_info['Symbol'] = cells[0].get_attribute('data-symbol')
            stock_info['Close Price'] = cells[1].text
            # stock_info['Change'] = cells[2].text
            # stock_info['Change (Absolute)'] = cells[3].text
            # stock_info['Recommendation'] = cells[4].text
            # stock_info['Volume'] = cells[5].text
            # stock_info['Value Traded'] = cells[6].text
            # stock_info['Market Cap'] = cells[7].text
            # stock_info['Price/Earnings (TTM)'] = cells[8].text
            # stock_info['Earnings Per Share (Basic TTM)'] = cells[9].text
            # stock_info['Number of Employees'] = cells[10].text
            # stock_info['Sector'] = cells[11].text
            
            top_three_stocks.append(stock_info)

        # Print the top three stocks
        for stock in top_three_stocks:
            print(stock)
        

        # switch to new tab fro zerodha login
        driver.switch_to.new_window('tab')
        zerodha__log__in(top_three_stocks)
    
        

    except NoSuchElementException:
        # Switch back to the original window
        print('----trading view value store from filter NoSuchElementException----')


    
