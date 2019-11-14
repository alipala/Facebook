from Locators.login import LoginLocators

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.email_textbox_name = LoginLocators.email_textbox_name
        self.password_textbox_name = LoginLocators.password_textbox_name
        self.login_button_id = LoginLocators.login_button_id

    def enter_login_details(self, email, password):
        # Enter email
        self.driver.find_element_by_name(self.email_textbox_name).clear()
        self.driver.find_element_by_name(self.email_textbox_name).send_keys(email)

        # Enter password
        self.driver.find_element_by_name(self.password_textbox_name).clear()
        self.driver.find_element_by_name(self.password_textbox_name).send_keys(password)

    def click_login_button(self):
        self.driver.find_element_by_id(self.login_button_id).click()
