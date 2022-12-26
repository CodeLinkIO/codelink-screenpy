from screenpy_selenium import Target

from ui.base.base_page import BasePage


class LoginPage(BasePage):

    USERNAME_INPUT = Target.the('The Username Input').located_by('#username')
    PASSWORD_INPUT = Target.the('The Password Input').located_by('#password')

    def __init__(self, url):
        super().__init__(url)
