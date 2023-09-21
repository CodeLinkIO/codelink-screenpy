from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from globals import constants


class Browser:
    __match_args__ = ('option',)

    def __init__(self, option):
        self.option = option

    def driver(self):
        raise NotImplementedError

    @staticmethod
    def construct_browser(request):
        option = request.config.option
        match option.browser.lower():
            case constants.CHROME:
                return Chrome(option=option)
            case constants.FIREFOX:
                return Firefox(option=option)
            case constants.EDGE:
                return Edge(option=option)


class Chrome(Browser):
    def driver(self):
        window_size = self.option.window_size
        headless = self.option.headless
        enable_har = self.option.enable_har

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(f'--window-size={window_size}')
        chrome_options.headless = headless
        chrome_options.add_experimental_option(
            "prefs", {"profile.content_settings.exceptions.clipboard": {'*': {'setting': 1}}}
        )

        selenium_wire_options = {
            'enable_har': enable_har  # Capture HAR data, retrieve with driver.har
        }

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=chrome_options,
            seleniumwire_options=selenium_wire_options)
        driver.implicitly_wait(5)

        return driver


class Firefox(Browser):
    def driver(self):
        # TODO: Firefox To be implemented
        raise NotImplementedError


class Edge(Browser):
    def driver(self):
        # TODO: Edge To be implemented
        raise NotImplementedError
