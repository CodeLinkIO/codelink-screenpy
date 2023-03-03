import typing
from retry import retry

from screenpy import Actor
from screenpy_selenium import Target
from screenpy.pacing import beat
from selenium.common import StaleElementReferenceException

from enums.asset_level import AssetLevel
from ui.asset_list_game import AssetListGamePage


class FavouriteAssetListData:

    def __init__(
            self,
            asset_level: AssetLevel
    ) -> None:
        self.asset_level = asset_level
        self.asset_value = asset_level.value

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

    @beat('{} examines the favourite {asset_value}s section on Assets List Game')
    def answered_by(self, the_actor: Actor) -> typing.List[str]:
        if self.asset_level == AssetLevel.FRANCHISE:
            return self.get_favourite_area_data(AssetListGamePage.FAVOURITE_FRANCHISE_NAME, the_actor)
        elif self.asset_level == AssetLevel.TITLE:
            return self.get_favourite_area_data(AssetListGamePage.FAVOURITE_TITLE_NAME, the_actor)
        raise AttributeError("Only Favourite Franchises and Favourite Titles supported")
