import typing
from itertools import filterfalse

import pytest
from _pytest.config import Config
from pytest import fixture
from screenpy.narration import StdOutAdapter
from screenpy.pacing import the_narrator
from screenpy_adapter_allure import AllureAdapter

from enums import TestLevels
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
    parser.addoption(
        '--level',
        type=lambda level: getattr(TestLevels, str(level).upper()),
        default=TestLevels.REGRESSION,
        choices=list(TestLevels),
        help='The test level to execute'
    )


def pytest_configure(config):
    """
    Includes markers and plugins available for tests
    """
    config.addinivalue_line(
        'markers',
        'level(value): mark test level (Regression Default)'
    )


def pytest_collection_modifyitems(config: Config, items: typing.List[pytest.Item]):

    current_level = config.getoption("level")

    def select_test(item):
        return all([
            select_by_level(item)
        ])

    def select_by_level(item: pytest.Item):
        level_marker = item.get_closest_marker("level")
        if level_marker and level_marker.args and current_level:
            level = level_marker.args[0]
            if type(level) in [TestLevels, int]:
                if type(level) == TestLevels:
                    level = level.value
                return level <= current_level.value
            else:
                raise TypeError("Invalid type specified in level marker")
        return True

    config.hook.pytest_deselected(items=filterfalse(select_test, items))
    items[:] = filter(select_test, items)
