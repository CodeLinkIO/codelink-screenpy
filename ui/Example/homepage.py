from screenpy_selenium import Target

from ui.base_page import BasePage


class HomePage(BasePage):

    SEARCH_INPUT = Target.the("Search Input").located_by("input[id='query']")
    SEARCH_BUTTON = Target.the("Search Button").located_by("input[data-disable-with='Search']")

    def __init__(self, url):
        super().__init__(url)
