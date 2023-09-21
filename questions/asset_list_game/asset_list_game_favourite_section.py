import typing

from retry import retry
from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium import Target
from selenium.common import StaleElementReferenceException

from ui.asset_list_game import AssetListGamePage


class AssetListGameFavouriteSection:

    def __init__(
            self,
            type: str
    ) -> None:
        self.type = type

    @staticmethod
    @retry(StaleElementReferenceException, tries=3, delay=1)
    def get_favourite_area_data(
            locator: Target,
            the_actor: Actor
    ) -> typing.List[str]:
        data = []
        for element in locator.all_found_by(the_actor):
            data.append(element.text)
        return data

    @beat('{} examines the favourite {type}s section on Assets List Game')
    def answered_by(self, the_actor: Actor) -> typing.List[str]:
        if self.type == "franchise":
            return self.get_favourite_area_data(AssetListGamePage.FAVOURITE_FRANCHISE_NAME, the_actor)
        elif self.type == "title":
            return self.get_favourite_area_data(AssetListGamePage.FAVOURITE_TITLE_NAME, the_actor)
        raise AttributeError("Only Favourite Franchises and Favourite Titles supported")
