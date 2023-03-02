from screenpy import Actor
from screenpy.pacing import beat

from actions.wait_click import WaitClick
from ui import AssetListGamePage


class ExpandTitle:

    def __init__(self, title: str) -> None:
        self.title = title

    @beat("{} expands title '{title}'.")
    def perform_as(self, the_actor: Actor) -> None:
        the_actor.attempts_to(
            WaitClick(AssetListGamePage.get_title_link(self.title))
        )
