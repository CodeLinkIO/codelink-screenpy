from screenpy_selenium import Target

from ui.base.base_page import BasePage


class LoginPage(BasePage):

    USERNAME_INPUT = Target.the('Username Input').located_by('#username')
    PASSWORD_INPUT = Target.the('Password Input').located_by('#password')
    LOG_IN_BUTTON = Target.the('Log In Button').located_by("input[class='login_button']")

    def __init__(self, url):
        super().__init__(url)
