import pytest


pytest_plugins = ['configs.driver_config']


@pytest.fixture
def env(request):
    return request.config.option.env


def pytest_addoption(parser):
    parser.addoption(
        '--browser', action='store', default='chrome',
        help='The browser to run the automation test, default: chrome')
    parser.addoption(
        '--window-size', action='store', default='1920,1080', dest='window_size',
        help='The windows size of the browser, default: 1920,1080')
    parser.addoption(
        '--headless', action='store_true',
        help='Enable headless mode')
    parser.addoption(
        '--enable-har', action='store_true', dest='enable_har',
        help='Enable HAR recording')
    parser.addoption(
        '--env', action='store', default='default',
        help='The environment to execute the test')

