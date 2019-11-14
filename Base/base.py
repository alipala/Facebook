import os
myPath = os.path.dirname(os.path.abspath(__file__))
import pytest
from selenium import webdriver
import allure


class Base:

    @pytest.fixture(autouse=True)
    def set_up(self):
        print("Initializing Chrome driver")
        print(myPath)
        self.driver = webdriver.Chrome(executable_path= myPath + "/" + "/chromedriver.exe")
        print("=================================")
        print("Test started")
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.facebook.com/")
        self.driver.maximize_window()

        yield self.driver
        if self.driver is not None:
            print("=================================")
            print("Tests finished")
            self.driver.close()
            self.driver.quit()

    def take_screenshot(self):
        # Allure screenshot for the test
        allure.attach(self.driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)