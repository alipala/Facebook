from Locators.home import HomeLocators


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.bookmark_icon_left_xpath = HomeLocators.bookmark_icon_left_xpath
        self.user_navigation_label_id = HomeLocators.user_navigation_label_id
        self.logout_span_xpath = HomeLocators.logout_span_xpath

    def logout(self):
        self.driver.find_element_by_id(self.user_navigation_label_id).click()
        self.driver.find_element_by_xpath(self.logout_span_xpath).click()

    def get_bookmark_icon_text(self):
        element = self.driver.find_element_by_xpath(self.bookmark_icon_left_xpath)
        return element.text
