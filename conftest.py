from pytest import fixture
from screenpy.pacing import the_narrator
from screenpy_adapter_allure import AllureAdapter
from screenpy.narration.adapters.stdout_adapter import StdOutAdapter

from globals.constants import ENVIRONMENTS_FILE_PATH
from utils.json_reader import read_file


pytest_plugins = ['configs.actor_config', 'configs.driver_config', 'configs.page_provider']

the_narrator.attach_adapter(AllureAdapter())
the_narrator.attach_adapter(StdOutAdapter())


@fixture
def env(request):
    return request.config.option.env or 'default'


@fixture
def env_data(env):
    return read_file(ENVIRONMENTS_FILE_PATH)


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
