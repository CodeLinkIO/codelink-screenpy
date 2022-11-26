from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.actions import Enter
from selenium.webdriver.common.keys import Keys

from ui.Example.homepage import HomePage


class SearchOnHomePage:

    def __init__(self, search_text: str):
        self.search_text = search_text

    @beat("{} searches for the text {search_text}.")
    def perform_as(self, the_actor: Actor) -> None:
        the_actor.attempts_to(
            Enter.the_keys(self.search_text).into_the(HomePage.SEARCH_INPUT),
            Enter.the_keys(Keys.ENTER).into_the(HomePage.SEARCH_INPUT)
        )

