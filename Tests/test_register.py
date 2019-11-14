import sys, os
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from Pages.RegisterPage import RegisterPage
from Base.base import Base
import allure
import pandas as pd


@allure.feature("Register Tests")
class TestRegister(Base):
    __failed_register_attempt_message = "Please choose a more secure password. " \
                                        "It should be longer than 6 characters, " \
                                        "unique to you and difficult for others to guess."

    __expected_url = "https://www.facebook.com/confirmemail.php?next=https%3A%2F%2Fwww.facebook.com%2F&rd"
    __user_data_file = r"\user_details.xlsx"
    df = pd.read_excel(os.getcwd() + __user_data_file)
    user_list = df.values.tolist()

    @allure.story("Successful register")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase(name="Testcase:4", url="https://www.facebook.com")
    def test_register_success(self):
        try:
            driver = self.driver
            register = RegisterPage(driver)
            register.enter_register_details(self.user_list[5])
            register.click_register_button()
            time.sleep(10)
            cur_url = driver.current_url
            assert cur_url == self.__expected_url # It should be forwarded to sign up
        except Exception as e:
            # Allure screenshot for the test
            allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)
            raise
            print("Title is wrong", format(e))

    @allure.story("Failed register")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase(name="Testcase:5", url="https://www.facebook.com")
    def test_register_fail(self):
        try:
            driver = self.driver
            register = RegisterPage(driver)
            register.enter_register_details(self.user_list[3])
            register.click_register_button()
            wait = WebDriverWait(driver, 10)
            element = wait.until(EC.visibility_of_element_located((By.XPATH, register.error_message_xpath)))
            assert self.__failed_register_attempt_message == element.text
        except NoSuchElementException as noe:
            # Allure screenshot for the test
            allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)
            raise
            print("Could not find the element", format(noe))
        except Exception as e:
            # Allure screenshot for the test
            allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)
            raise
            print("Registration fail!", format(e))
