import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Base.base import Base
from selenium.webdriver.chrome.options import Options
import pytest
import allure
import pandas as pd

# Disable notifications while trying to log in
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")


@allure.feature("Login Tests")
@pytest.mark.usefixtures('set_up')
class TestLogin(Base):

    # Failed login attempt url
    __expected_url = "https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=110"
    __expected_non_user_url = "https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=100"
    __test_case_url = "https://www.facebook.com"

    # Installed xlrd package to read the .xlsx file
    __user_data_file = r"\user_details.xlsx"

    df = pd.read_excel(os.getcwd() + __user_data_file)

    @allure.story("Successful login")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase(name="Testcase:1", url=__test_case_url)
    def test_login_success(self):
        try:
            driver = self.driver
            self.login_attempt(self.df.loc[0, "mobile_email"], self.df.loc[0, "password"])
            home = HomePage(driver) # Homepage object
            name = self.df.loc[0, "firstname"] + " " + self.df.loc[0, "lastname"]
            Base.take_screenshot(self)
            assert home.get_bookmark_icon_text() == name
        except Exception as e:
            # Allure screenshot for the test
            allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)
            raise
            print("Title is wrong", format(e))

    @allure.story('Failed login with wrong password')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase(name="Testcase:2", url=__test_case_url)
    def test_login_wrong_password(self):
        try:
            driver = self.driver
            self.login_attempt(self.df.loc[3, "mobile_email"], self.df.loc[3, "password"])
            cur_url = driver.current_url
            assert self.__expected_url == cur_url # It should be forwarded to url, if login failed
        except Exception as e:
            # Allure screenshot for the test
            allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)
            raise
            print("Wrong credential login problem occured", format(e))

    @allure.story('Failed login with empty email and password')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.testcase(name="Testcase:3", url=__test_case_url)
    def test_login_empty_credential(self):
        try:
            driver = self.driver
            self.login_attempt("", "")
            cur_url = driver.current_url
            assert self.__expected_url == cur_url # It should be forwarded to url, if login failed
        except Exception as e:
            # Allure screenshot for the test
            allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)
            raise
            print("Empty fields login problem occured", format(e))

    @allure.story('Failed login with a user who has not an account')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.testcase(name="Testcase:4", url=__test_case_url)
    def test_login_not_facebook_user(self):
        try:
            driver = self.driver
            self.login_attempt(self.df.loc[6, "mobile_email"], self.df.loc[6, "password"])
            cur_url = driver.current_url
            assert self.__expected_non_user_url == cur_url # It should be forwarded to url, if login failed
        except Exception as e:
            # Allure screenshot for the test
            allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)
            raise
            print("There is no such user problem occured", format(e))

    # Helper function
    def login_attempt(self, email, password):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_login_details(email, password)
        login.click_login_button()
