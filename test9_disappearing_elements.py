import time
import unittest
import urllib3
import requests
import pyautogui
from pynput.keyboard import Key, Controller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = Service("C:\\Users\\mariu\\chromedriver.exe")
url = "https://the-internet.herokuapp.com/"


class DisappearingElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=PATH)
        driver = self.driver
        driver.get(url)
        driver.maximize_window()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/ul/li[9]/a").click()
    
    def test_1(self):
        driver = self.driver
    
    def tearDown(self):
        pass
        # self.driver.quit()


if __name__ == '__main__':
    unittest.main()
