import time
from retry import retry

from screenpy import Actor
from screenpy.pacing import beat
from selenium.common import StaleElementReferenceException

from ui.asset_list_game import AssetListGamePage


class AssetListGameHomePageData:

    TIMEOUT = 10
    ASSETS_LEVEL_ELEMENTS_MAPPING = {
        "franchise": AssetListGamePage.FRANCHISE_NAME,
        "title": AssetListGamePage.TITLE_NAME,
        "beat": AssetListGamePage.BEAT_NAME
    }

    def __init__(
            self,
            type: str,
            num_records: int
    ) -> None:
        self.type = type
        self.num_records = num_records
        self.actual_records = 0

    @retry(StaleElementReferenceException, tries=3, delay=1)
    def get_assets_list_data(
            self,
            the_actor: Actor
    ) -> list:
        data = []
        for element in self.ASSETS_LEVEL_ELEMENTS_MAPPING.get(self.type).all_found_by(the_actor):
            data.append(element.text)
        return sorted(data)

    @beat('{} examines the data on Assets List Game')
    def answered_by(self, the_actor: Actor):
        end_time = time.time() + self.TIMEOUT
        while time.time() <= end_time:
            self.actual_records = len(self.ASSETS_LEVEL_ELEMENTS_MAPPING.get(self.type).all_found_by(the_actor))
            if self.actual_records == self.num_records:
                return self.get_assets_list_data(the_actor)
            time.sleep(0.5)
        raise TimeoutError(f"The number of displayed {self.type}s records does not match "
                           f"after waiting {self.TIMEOUT} seconds. "
                           f"Actual: {self.actual_records} != Expected: {self.num_records}")
