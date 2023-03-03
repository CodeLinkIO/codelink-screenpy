from screenpy import Actor
from screenpy.pacing import beat

from actions import WaitClick
from ui import AssetListGamePage


class FavouriteFranchise:

    def __init__(self, franchise: str) -> None:
        self.franchise = franchise

    @beat("{} favourites franchise '{franchise}'.")
    def perform_as(self, the_actor: Actor) -> None:
        the_actor.attempts_to(
            WaitClick(AssetListGamePage.get_franchise_favourite_icon(self.franchise))
        )
