from enum import Enum

from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.actions import Click

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
            disabled: bool = False
    ):
        self.filter_type = filter_type
        self.filter_type_value = filter_type.value
        self.disabled = disabled
        self.filter_value = "disabled" if self.disabled else "enabled"

    def set_filter(self, the_actor: Actor):
        toggle = self.FILTER_ELEMENTS_MAPPING.get(self.filter_type).found_by(the_actor)
        is_toggle_enabled = "75" in toggle.value_of_css_property("background-color")
        if is_toggle_enabled == self.disabled:
            the_actor.attempts_to(
                Click.on_the(self.FILTER_ELEMENTS_MAPPING.get(self.filter_type))
            )

    @beat("{} filters '{filter_type_value}' as {filter_value}.")
    def perform_as(self, the_actor: Actor) -> None:
        the_actor.attempts_to(
            WaitClick(AssetListGamePage.MASTER_FILTER)
        )
        self.set_filter(the_actor)
        the_actor.attempts_to(
            Click.on_the(AssetListGamePage.MASTER_FILTER)
        )
