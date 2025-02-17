import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import TimeoutException


# PATH = Service("C:\\Users\\marius\\chromedriver.exe")
chrome_service = Service(ChromeDriverManager().install())
url = "https://the-internet.herokuapp.com/"

# Test data
title = "Context Menu"
text1 = "Context menu items are custom additions that appear in the right-click menu."
text2 = "Right-click in the box below to see one called 'the-internet'. When you click it, it will trigger a JavaScript alert."
alert_text = "You selected a context menu"


class ContextMenu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=chrome_service)
        self.driver.get(url)
        self.driver.maximize_window()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Context Menu']").click()

    def test_title_text(self):
        paragraph = self.driver.find_elements(By.TAG_NAME, "p")
        self.assertEqual(self.driver.find_element(By.TAG_NAME, "h3").text, title)
        self.assertEqual(paragraph[0].text, text1)
        self.assertEqual(paragraph[1].text, text2)
        
    def test_box_properties(self):
        style = self.driver.find_element(By.ID, "hot-spot").get_attribute("style")
        self.assertEqual(style, "border-style: dashed; border-width: 5px; width: 250px; height: 150px;")

    def test_alert_box_open(self):
        alert = Alert(self.driver)
        action = ActionChains(self.driver)
        box = self.driver.find_element(By.ID, "hot-spot")
        action.context_click(box).perform()
        self.assertEqual(alert.text, alert_text)

    def test_alert_box_closed(self):
        alert = Alert(self.driver)
        action = ActionChains(self.driver)
        box = self.driver.find_element(By.ID, "hot-spot")
        action.context_click(box).perform()
        self.assertEqual(alert.text, alert_text)
        alert.accept()
        try:
            WebDriverWait(self.driver, 2).until(EC.alert_is_present())
        except TimeoutException:
            alert_is_present = 'No'
        else:
            alert_is_present = 'Yes'
        finally:
            self.assertTrue(alert_is_present == 'No')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
