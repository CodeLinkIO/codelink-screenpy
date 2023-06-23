from enum import Enum

from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.abilities import BrowseTheWeb
from screenpy_selenium.actions import Click

from ui import YoutubeHubPage


class SortMasterAssetColumn(Enum):
    BEAT = 'Beat'
    MASTER_NAME = 'Master Name'
    GO_LIVE_DATE = 'Go Live Date'


class SortMasterAsset:

    def __init__(
            self,
            column: SortMasterAssetColumn,
            ascending: bool = True
    ):
        self.column = column
        self.sort_value = 'ascending' if ascending else 'descending'

    @beat("{} sorts Master Asset Table with column '{column}'.")
    def perform_as(self, the_actor: Actor) -> None:
        driver = the_actor.ability_to(BrowseTheWeb).browser
        column_header_element = YoutubeHubPage.get_master_asset_table_header(self.column.value)
        retries = 0
        while retries < 3:
            actual_sort = column_header_element.found_by(the_actor).get_attribute("aria-sort")
            if actual_sort != self.sort_value:
                the_actor.attempts_to(
                    Click.on_the(column_header_element)
                )
                driver.implicitly_wait(0.5)
            else:
                break
            retries += 1
