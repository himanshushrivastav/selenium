import os
import time
from traceback import print_stack
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utility.customLogger import loggers
from utility.Webdriver_manager import selenium_driver


class fun(selenium_driver):
    logs = loggers()
    def __init__(self):

        super(selenium_driver, self).__init__()

    def byLocator(self, locator = 'xpath'):
        type =str(locator).lower()

        if type == 'css':
            return By.CSS_SELECTOR
        elif type == 'xpath':
            return By.XPATH
        elif type == 'class':
            return By.CLASS_NAME
        elif type == 'id':
            return By.ID

        else:
            self.logs.error('locator type is not correct')

    def element(self,locator,  locatortype = 'xpath'):
        try:
            element = self.driver.find_element(self.byLocator(locatortype), locator)
            self.logs.info(locator + "found on page")
            return element
        except:
            self.logs.error(locator + ' is missing on page')
            return False

    def click(self,locator, locatorType = 'xpath'):
        try:
            self.element(locator=locator, locatortype=locatorType).click()
            return True
        except:
            return False

    def sendkeys(self,locator,data, locatorType = 'xpath'):
        try:
            self.element(locator).send_keys(data)
            return True
        except:
            return False


    def select(self,locator,option,optionType = 'text', locatortype = 'xpath'):
        try:
            select = Select(self.element(locator=locator, locatortype = locatortype ))
            optiontype = str(optionType).lower()

            if optiontype == 'index':
                select.deselect_by_index(option)

            elif optiontype == 'text':
                select.deselect_by_visible_text(option)
            elif optiontype == 'value':
                select.deselect_by_value(option)

            else:
                self.logs.info("please give some option type in option or" +"option"+ "is not able to select")
        except:
            self.logs.error("not able to select locator -> " + locator)

    def wait(self,locator, locatorType = 'xpath'):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((self.byLocator(locator=locatorType), locator))
            )
        finally:
            self.logs.error(locator + 'is not present on the page')
            return False


    def doubleClick(self,locator, locatorType = 'xpath'):
        try:
            Action = ActionChains(self.driver)
            Action.double_click(locator)
            return True
        finally:
            self.logs.error(locator + " is Not present on Page")
            return False

    def click_in_frame(self,locator, locatorType = 'xpath'):
        try:
            self.driver.switch_to.frame(self.click(locator=locator, locatorType=locatorType))
        except:
            self.logs.error("frame element ->" + locator+ "is not on page")
            return False

    def screenShot(self, resultMessage):
        """
        Take a screenshot of the current open web page
        """
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        if len(fileName) >= 200:
            fileName = str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)

            self.logs.info("Screenshot save to directory: " + destinationFile)
        except:
            self.logs.error("### Exception Occurred when taking screenshot")
            print_stack()