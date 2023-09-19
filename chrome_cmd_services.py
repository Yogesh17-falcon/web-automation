from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import subprocess
from selenium.common.exceptions import NoSuchElementException


try:
    chrome_cmd_command = r'"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\Yogesh\Shitty Projects\Automation\Dumping Data"'
    subprocess.Popen(chrome_cmd_command, shell=True)

    options = Options()
    options.add_experimental_option("debuggerAddress", "localhost:9222")  # Use the correct debugger address

    service = Service(executable_path='C:/Yogesh/Shitty Projects/Automation/chromedriver.exe')
    driver = webdriver.Chrome(service=service,options=options)

except NoSuchElementException:
    print("check chrome_cmd_service and connection...")