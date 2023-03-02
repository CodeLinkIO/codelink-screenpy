from datetime import datetime
from retry import retry

from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.actions import Enter, Wait, Click, Chain, Hover
from screenpy_selenium import Target
from selenium.common import StaleElementReferenceException

from ui import AssetListGamePage


class EditBeat:

    DATE_FMT = "%m/%d/%Y"

    def __init__(
            self,
            name: str = None,
            phase: str = None,
            start_date: datetime = None,
            end_date: datetime = None,
            is_evergreen: bool = False
    ):
        self.name = name
        self.phase = phase
        self.start_date = start_date
        self.end_date = end_date
        self.is_evergreen = is_evergreen

    def set_date(
            self,
            the_actor: Actor,
            date: datetime,
            locator: Target
    ):
        the_actor.attempts_to(
            Enter.the_text(date.strftime(self.DATE_FMT)).into_the(locator),
            Click.on_the(AssetListGamePage.BEAT_MODAL_HEADER)  # Close the date picker
        )

    def set_evergreen(self, the_actor: Actor):
        evergreen_element = AssetListGamePage.BEAT_MODAL_IS_EVERGREEN_FILL.found_by(the_actor)
        actual_is_evergreen = evergreen_element.get_attribute("fill") is not None
        if actual_is_evergreen != self.is_evergreen:
            the_actor.attempts_to(
                Click.on_the(AssetListGamePage.BEAT_MODAL_IS_EVERGREEN_CHECKBOX)
            )

    @beat("{} edits beat.")
    @retry(StaleElementReferenceException, tries=10, delay=1)
    def perform_as(self, the_actor: Actor) -> None:
        the_actor.attempts_to(
            Chain(
                Hover.on_the(AssetListGamePage.VIEW_BEAT_LINK),
                Click.on_the(AssetListGamePage.EDIT_BEAT_BUTTON)),
            Wait.for_the(AssetListGamePage.BEAT_MODAL_HEADER)
        )
        if self.name:
            the_actor.attempts_to(
                Enter.the_text(self.name).into_the(AssetListGamePage.BEAT_MODAL_NAME_INPUT)
            )
        if self.phase:
            the_actor.attempts_to(
                Enter.the_text(self.phase).into_the(AssetListGamePage.BEAT_MODAL_PHASE_DROPDOWN)
            )
        if self.start_date:
            self.set_date(the_actor, self.start_date, AssetListGamePage.BEAT_MODAL_START_DATE_INPUT)
        if self.end_date:
            self.set_date(the_actor, self.end_date, AssetListGamePage.BEAT_MODAL_END_DATE_INPUT)
        self.set_evergreen(the_actor)
        the_actor.attempts_to(
            Click.on_the(AssetListGamePage.BEAT_MODAL_SAVE_BUTTON)
        )
