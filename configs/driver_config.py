import pytest
from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver(request):
    yield initiate_driver(request)


def initiate_driver(request):
    window_size = request.config.option.window_size
    headless = request.config.option.headless
    enable_har = request.config.option.enable_har

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f'--window-size={window_size}')
    chrome_options.headless = headless

    selenium_wire_options = {
        'enable_har': enable_har  # Capture HAR data, retrieve with driver.har
    }

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=chrome_options,
        seleniumwire_options=selenium_wire_options)
    driver.implicitly_wait(5)

    return driver
