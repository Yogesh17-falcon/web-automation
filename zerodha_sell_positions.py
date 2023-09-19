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
from sets_quantity_price import quantity__for__sell,price__for__sell




def zerodha__sell__positions():

    try:
           # after loop end we can shift to position tab and check for positions or order exist or not 
        # if exist we can place order sell order
        positions_link_text = "Positions"
        positions_link = driver.find_element(By.LINK_TEXT,positions_link_text)
        positions_link.click()
        time.sleep(2)

        # ---------------empty position check-----------#

        try:
            # element = driver.find_element(By.XPATH, "//p[contains(text(), 'You don't have any positions yet')]")
            check_element = driver.find_element(By.CLASS_NAME,"open-positions") 
            print("positions exist.")
            time.sleep(5)
            all_postions = []
            table_rows = driver.find_elements(By.CSS_SELECTOR, 'tbody tr')

    # Loop through each row to extract and print the information
            for row in table_rows:
            
                # Extract relevant information from the row
                
                product = row.find_element(By.CSS_SELECTOR, 'td.open.product').text.strip()
                quantity = row.find_element(By.CSS_SELECTOR, 'td.text-buy.open.quantity.right').text.strip()
                avg_price = row.find_element(By.CSS_SELECTOR, 'td.open.average-price.right').text.strip()
                last_price = row.find_element(By.CSS_SELECTOR, 'td.open.last-price.right').text.strip()
                pnl = row.find_element(By.CSS_SELECTOR, 'td.open.pnl.right span').text.strip()
                change_percent = row.find_element(By.CSS_SELECTOR, 'td.open.change-percent.change-percent.right span').text.strip()

                # Print the extracted information in the desired format
                # print(f"{product} {quantity} {avg_price} {last_price} {pnl} {change_percent}")
                # Create a dictionary for the position information
                position_info = {'product': product, 'quantity': quantity, 'avg_price': avg_price, 'last_price': last_price, 'pnl': pnl, 'change_percent': change_percent}

                # Append the position information to the list
                all_postions.append(position_info)

                #-------------------i am checking code here----------------------------------#
                
                
                actions = ActionChains(driver)
                actions.move_to_element(row).perform()

                options_button = row.find_element(By.XPATH, './/span[@class="context-menu-button"]')
                options_button.click()

                time.sleep(2)

                    

                exit_button = driver.find_element(By.XPATH, '//li/a[contains(text(), "Exit")]')
                exit_button.click()

                time.sleep(5)
                form_element = driver.find_element(By.CLASS_NAME, 'order-window')
                form_element.click()
                # Locate the "From" option using the CSS selector
                
                time.sleep(3)
                # limit_order_label = form_element.find_element(By.XPATH, '//label[@for="radio-137"]')
                limit_order_label = form_element.find_element(By.XPATH, '//label[contains(text(), "Limit")]')
                limit_order_label.click()
                
                
                quantity_element = form_element.find_element(By.XPATH, '//input[@label="Qty."]')
                # quantity_store = quantity_element.get_attribute('value')
                quantity_element.clear()
                # quantity_element.send_keys("1")
                quantity_element.send_keys(str(quantity__for__sell))


                # Capture the last price value
                # last_price_element = form_element.find_element(By.XPATH, '//span[@class="last-price"]')
                last_price_element = driver.find_element(By.XPATH,"//div[@class='exchange su-radio-wrap checked']/label/span[@class='last-price']")

                # last_price_store = last_price_element.text
                last_price_store = float(last_price_element.text.strip("₹"))

                # desired_price = last_price_store + 1
                desired_price = last_price_store + price__for__sell
                # print(desired_price)

                price_input_element = form_element.find_element(By.XPATH, '//input[@label="Price"]')
                price_input_element.send_keys(Keys.BACKSPACE * len(price_input_element.get_attribute('value')))
                price_input_element.send_keys(str(desired_price))


                # Submit the form or perform other actions as needed
                # Example: Click the "Submit" button
                submit_button = form_element.find_element(By.CLASS_NAME, 'submit')
                submit_button.click()






                #-----------------------------------------------------------------------------#
            

        # print(all_postions)
        # print(all_postions[0])
        # print(all_postions[1])


        except:
            print("positions not exist.")

            # -----------------------------------------------#
                
        
    except NoSuchElementException:
        print('----zerodha sell positions in NoSuchElementException----')



