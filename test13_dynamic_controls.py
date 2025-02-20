import unittest
import urllib3
import requests
import pyautogui
from time import sleep
from pynput.keyboard import Key, Controller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


PATH = Service("C:\\Users\\marius\\chromedriver.exe")
# chrome_service = Service(ChromeDriverManager().install())
url = "https://the-internet.herokuapp.com/"

# action_chains = ActionChains(driver)
# alert = Alert(driver)

# test data


class TestDynamicControls(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=PATH)
        self.driver.get(url)
        self.driver.maximize_window()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        self.driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[13]/a').click()
    
    def test_x(self):
        # locators, waits, actions
        self.assertEqual(1, 1)
    
    def test_y(self):
        # locators, waits, actions
        self.assertEqual(True, False)
    
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
