import time
from retry import retry

from screenpy import Actor
from screenpy.pacing import beat
from selenium.common import StaleElementReferenceException

from enums.asset_level import AssetLevel
from ui.asset_list_game import AssetListGamePage


class AssetListData:

    TIMEOUT = 10
    ASSETS_LEVEL_ELEMENTS_MAPPING = {
        AssetLevel.FRANCHISE: AssetListGamePage.FRANCHISE_NAME,
        AssetLevel.TITLE: AssetListGamePage.TITLE_NAME,
        AssetLevel.BEAT: AssetListGamePage.BEAT_NAME
    }

    def __init__(
            self,
            asset_level: AssetLevel,
            num_records: int
    ) -> None:
        self.asset_level = asset_level
        self.num_records = num_records
        self.actual_records = 0

    @retry(StaleElementReferenceException, tries=3, delay=1)
    def get_assets_list_data(
            self,
            the_actor: Actor
    ) -> list:
        data = []
        for element in self.ASSETS_LEVEL_ELEMENTS_MAPPING.get(self.asset_level).all_found_by(the_actor):
            data.append(element.text)
        return data

    @beat('{} examines the data on Assets List Game')
    def answered_by(self, the_actor: Actor):
        end_time = time.time() + self.TIMEOUT
        while time.time() <= end_time:
            self.actual_records = len(self.ASSETS_LEVEL_ELEMENTS_MAPPING.get(self.asset_level).all_found_by(the_actor))
            if self.actual_records == self.num_records:
                return self.get_assets_list_data(the_actor)
            time.sleep(0.5)
        raise TimeoutError(f"The number of displayed {self.asset_level.value}s records does not match "
                           f"after waiting {self.TIMEOUT} seconds. "
                           f"Actual: {self.actual_records} != Expected: {self.num_records}")
