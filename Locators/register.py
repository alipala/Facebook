class RegisterLocators:

    first_name_textbox_name = "firstname"
    last_name_textbox_name = "lastname"
    mobile_email_textbox_name = "reg_email__"
    re_mobile_email_textbox_name = "reg_email_confirmation__"
    password_textbox_name = "reg_passwd__"
    birthday_day_select_name = "birthday_day"
    birthday_month_select_name = "birthday_month"
    birthday_year_select_name = "birthday_year"
    female_sex_radio_xpath = "//*[contains(text(),'Female')]"

    # if the sex is selected as  custom, these will be visible
    preferred_pronoun_select_name = "preferred_pronoun"
    custom_gender_textbox_name = "custom_gender"

    # submit button
    submit_button_name = "websubmit"

    # register error message
    error_message_xpath = '//*[@id="reg_error_inner"]'
