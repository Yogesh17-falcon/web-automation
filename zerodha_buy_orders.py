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
from sets_quantity_price import quantity__for__buy,price__for__buy



def zerodha__buy__orders():
    # print('from zerodha_buy_orders:',stock)

    try:
            # Buy stock
            symbol_element = driver.find_element(By.CLASS_NAME,'nice-name')
                
            # Hover over the symbol element
            action = ActionChains(driver)
            action.move_to_element(symbol_element).perform()
                
            # Wait for the buy button to appear after hovering
            time.sleep(2)  # Adjust the sleep time as needed
                

            # Click on the buy button
            buy_button_element = driver.find_element(By.CLASS_NAME,'buy')  # Replace with the actual buy button ID
            buy_button_element.click()


            # if we need to change intraday and limit then we need to click on form first
            # NOTEs : first we need to click form is necessary

            # time.sleep(3)
            # form_element = driver.find_element(By.CLASS_NAME, 'order-window')
            # form_element.click()
                    
            # time.sleep(2)
            # intraday_order_label = form_element.find_element(By.XPATH, '//label[@for="radio-132"]')
            # intraday_order_label.click()

            # time.sleep(2)
            # limit_order_label = form_element.find_element(By.XPATH, '//label[@for="radio-139"]')
            # limit_order_label.click()
                    

            time.sleep(3)
            
            quantity_input_element = driver.find_element(By.CSS_SELECTOR,"input[label='Qty.']")
            quantity_input_element.clear()
            # quantity_input_element.send_keys("2")
            # setting quantity here
            quantity_input_element.send_keys(str(quantity__for__buy))

            last_price_element = driver.find_element(By.XPATH,"//div[@class='exchange su-radio-wrap checked']/label/span[@class='last-price']")
            last_price = float(last_price_element.text.strip("₹").replace(',', ''))
            # print(last_price)
            # desired_price = last_price - 3
            # setting price here 
            desired_price = last_price - price__for__buy

            price_input_element = driver.find_element(By.CSS_SELECTOR,"input[label='Price']")
            price_input_element.clear()
            price_input_element.send_keys(str(desired_price))

               
            # this is for nudge : its working  

            try:
                popup_element = driver.find_element(By.CSS_SELECTOR, '.popup')
                # print('popup_element exists')
                cancel_button_element = driver.find_element(By.CSS_SELECTOR,".cancel")
                cancel_button_element.click()
            except:
                # print('popup_element does not exist')
                buy_button_element = driver.find_element(By.CSS_SELECTOR,".submit")
                buy_button_element.click()
                 



            # buy_button_element = driver.find_element(By.CSS_SELECTOR,".submit")
            # buy_button_element.click()

         
            
            time.sleep(5)

            action = ActionChains(driver)
            action.move_to_element(symbol_element).perform()

            remove_button_element = driver.find_element(By.CLASS_NAME,'icon-trash')  # Replace with the actual buy button ID
            remove_button_element.click()
            
            time.sleep(3)


    except NoSuchElementException:
        print('----zerodha Buy orders in NoSuchElementException----')