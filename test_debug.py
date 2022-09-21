import time
import unittest
import urllib3
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from pynput.keyboard import Key, Controller

PATH = Service("C:\\Users\\mariu\\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)

broken_images = 0

driver.get("https://the-internet.herokuapp.com/broken_images")
driver.maximize_window()

image_list = driver.find_elements(by=By.TAG_NAME, value="img")

for image in image_list:
    response = requests.get(image.get_attribute('src'), stream=True)
    if response.status_code != 200:
        broken_images += 1

driver.quit()

print(f"The number of broken images is: {broken_images}.")
