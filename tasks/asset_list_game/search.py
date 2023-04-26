from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.actions import Enter, Wait, Clear

from ui import AssetListGamePage


class Search:

    def __init__(self, keyword: str):
        self.keyword = keyword

    @beat("{} searches for Beat, Title or Franchise with keyword '{keyword}'.")
    def perform_as(self, the_actor: Actor, ) -> None:
        the_actor.attempts_to(
            Wait.for_the(AssetListGamePage.SEARCH_INPUT),
            Clear.the_text_from_the(AssetListGamePage.SEARCH_INPUT),
            Enter.the_text(self.keyword).into_the(AssetListGamePage.SEARCH_INPUT)
        )
