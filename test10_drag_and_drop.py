# delete unused imports
import time
import unittest
import urllib3
import requests
import pyautogui
from time import sleep
from pynput.keyboard import Key, Controller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException

PATH = Service("C:\\Users\\mariu\\chromedriver.exe")
# s = Service(ChromeDriverManager().install())

# driver = webdriver.Chrome(service=PATH)
# driver = webdriver.Chrome(service=s)

url = "https://the-internet.herokuapp.com/"

# action_chains = ActionChains(driver)
# alert = Alert(driver)
# test data here


class DragAndDrop(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=PATH)
        driver = self.driver
        driver.get(url)
        driver.maximize_window()
    
    def test_drag_A_on_B(self):
        driver = self.driver
        # locators, waits, actions here
        self.assertEqual(1, 1)
    
    def test_drag_B_on_A(self):
        driver = self.driver
        # locators, waits, actions here
        self.assertEqual(1, 1)
    
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()