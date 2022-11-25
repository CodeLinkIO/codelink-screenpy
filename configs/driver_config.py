import pytest
from configs.supported_browsers.browsers import Browser, Chrome, Edge, Firefox


@pytest.fixture
def driver(request):
    yield initiate_driver(request)


def initiate_driver(request):
    browser: Browser = Browser.construct_browser(request)
    match browser:
        case Chrome(request.config.option) as chrome:
            return chrome.driver()
        case Firefox(request.config.option) as firefox:
            return firefox.driver()
        case Edge(request.config.option) as edge:
            return edge.driver()
