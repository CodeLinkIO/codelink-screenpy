from screenpy import Actor
from screenpy.pacing import beat

from actions.wait_click import WaitClick
from ui import AssetListGamePage


class FavouriteTitle:

    def __init__(self, title: str) -> None:
        self.title = title

    @beat("{} favourites title '{title}'.")
    def perform_as(self, the_actor: Actor) -> None:
        the_actor.attempts_to(
            WaitClick(AssetListGamePage.get_title_favourite_icon(self.title))
        )
