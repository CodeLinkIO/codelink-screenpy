from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.actions import Clear, Click, Enter, Wait

from ui import YoutubeHubPage


class SearchMasterAsset:

    def __init__(
            self,
            keyword: str
    ):
        self.keyword = keyword

    @beat("{} searches for Master Asset ID with keyword '{keyword}'.")
    def perform_as(self, the_actor: Actor) -> None:
        locator = YoutubeHubPage.SEARCH_MASTER_ASSET_ID_INPUT
        the_actor.attempts_to(
            Wait.for_the(locator),
            Clear.the_text_from_the(locator),
            Enter.the_text(self.keyword).into_the(locator),
            Click.on_the(YoutubeHubPage.SEARCH_MASTER_ASSET_ID_ICON),
            Wait(20).seconds_for_the(YoutubeHubPage.SMALL_LOADING_ICON).to_disappear()
        )
