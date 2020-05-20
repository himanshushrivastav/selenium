import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class selenium_driver:
    """ This class is responsible to return driver instance"""
    def __init__(self):

        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def setup(self):
        self.driver.get(r'https://phptravels.org/clientarea.php')
        self.driver.maximize_window()
        self.driver.execute_script("document.body.style.zoom='100%'")



