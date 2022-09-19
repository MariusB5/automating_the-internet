import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = Service("C:\\Users\\mariu\\chromedriver.exe")
title = "Welcome to the-internet"
subtitle = "Available Examples"
url = "https://the-internet.herokuapp.com/"


class Sanity(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=PATH)
        driver = self.driver
        driver.maximize_window()
        driver.get(url)
    
    def test_homepage_reached(self):
        driver = self.driver
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        self.assertEqual(driver.find_element(by=By.TAG_NAME, value="h1").text, title)
        self.assertEqual(driver.find_element(by=By.TAG_NAME, value="h2").text, subtitle)
    
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()