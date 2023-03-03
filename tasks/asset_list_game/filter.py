from enum import Enum

from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.actions import Wait, Click

from actions import WaitClick
from ui import AssetListGamePage


class FilterType(Enum):
    SHOW_ONLY_ACTIVE_TITLES = "Show Only Active Titles"
    SHOW_ONLY_EA_TITLES = "Show Only EA Titles"
    SHOW_ADDITIONAL_CONTENT = "Show Additional Content"


class Filter:

    FILTER_ELEMENTS_MAPPING = {
        FilterType.SHOW_ONLY_ACTIVE_TITLES: AssetListGamePage.MASTER_FILTER_ACTIVE_TITLES_TOGGLE,
        FilterType.SHOW_ONLY_EA_TITLES: AssetListGamePage.MASTER_FILTER_EA_TITLES_TOGGLE,
        FilterType.SHOW_ADDITIONAL_CONTENT: AssetListGamePage.MASTER_FILTER_ADDITIONAL_CONTENT_TOGGLE
    }

    def __init__(
            self,
            filter_type: FilterType,
            num_active_filters: int
    ):
        self.filter_type = filter_type
        self.filter_type_value = filter_type.value
        self.num_active_filters = num_active_filters

    @beat("{} clicks on '{filter_type_value}' toggle.")
    def perform_as(self, the_actor: Actor) -> None:
        the_actor.attempts_to(
            WaitClick(AssetListGamePage.MASTER_FILTER),
            Click.on_the(self.FILTER_ELEMENTS_MAPPING.get(self.filter_type)),
            Wait.for_the(AssetListGamePage.get_num_filters_enabled_label(self.num_active_filters)),
            Click.on_the(AssetListGamePage.MASTER_FILTER)
        )
