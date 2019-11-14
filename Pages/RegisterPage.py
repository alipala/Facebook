from Locators.register import RegisterLocators
from selenium.webdriver.support.ui import Select
import time


class RegisterPage:

    def __init__(self, driver):
        self.driver = driver
        self.first_name_textbox_name = RegisterLocators.first_name_textbox_name
        self.last_name_textbox_name = RegisterLocators.last_name_textbox_name
        self.mobile_email_textbox_name = RegisterLocators.mobile_email_textbox_name
        self.re_mobile_email_textbox_name = RegisterLocators.re_mobile_email_textbox_name
        self.password_textbox_name = RegisterLocators.password_textbox_name
        self.birthday_day_select_name = RegisterLocators.birthday_day_select_name
        self.birthday_month_select_name = RegisterLocators.birthday_month_select_name
        self.birthday_year_select_name = RegisterLocators.birthday_year_select_name
        self.female_sex_radio_xpath = RegisterLocators.female_sex_radio_xpath
        self.preferred_pronoun_select_name = RegisterLocators.preferred_pronoun_select_name
        self.custom_gender_textbox_name = RegisterLocators.custom_gender_textbox_name
        self.submit_button_name = RegisterLocators.submit_button_name
        self.error_message_xpath = RegisterLocators.error_message_xpath

    def enter_register_details(self, user_list):
        # Enter first name
        self.driver.find_element_by_name(self.first_name_textbox_name).clear()
        self.driver.find_element_by_name(self.first_name_textbox_name).send_keys(user_list[0])

        # Enter last name
        self.driver.find_element_by_name(self.last_name_textbox_name).clear()
        self.driver.find_element_by_name(self.last_name_textbox_name).send_keys(user_list[1])

        # Enter email
        self.driver.find_element_by_name(self.mobile_email_textbox_name).clear()
        self.driver.find_element_by_name(self.mobile_email_textbox_name).send_keys(user_list[2])
        time.sleep(2)

        # Re enter email
        self.driver.find_element_by_name(self.re_mobile_email_textbox_name).clear()
        self.driver.find_element_by_name(self.re_mobile_email_textbox_name).send_keys(user_list[2])

        # Enter password
        self.driver.find_element_by_name(self.password_textbox_name).clear()
        self.driver.find_element_by_name(self.password_textbox_name).send_keys(user_list[3])

        # Fill birthday areas
        select_date = Select(self.driver.find_element_by_name(self.birthday_day_select_name))
        select_date.select_by_index("12")
        select_month = Select(self.driver.find_element_by_name(self.birthday_month_select_name))
        select_month.select_by_value("1")
        select_year = Select(self.driver.find_element_by_name(self.birthday_year_select_name))
        select_year.select_by_value("1995")

        # Check female radio
        sex_radio = self.driver.find_element_by_xpath(self.female_sex_radio_xpath)
        sex_radio.click()

    def click_register_button(self):
        self.driver.find_element_by_name(self.submit_button_name).click()

