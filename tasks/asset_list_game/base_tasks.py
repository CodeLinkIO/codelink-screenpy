from datetime import datetime

from screenpy import Actor
from screenpy_selenium.actions import Enter, Click
from screenpy_selenium import Target

from ui import AssetListGamePage


class BaseTasks:

    DATE_FMT = "%m/%d/%Y"

    # Add/Edit Beat Modal
    def set_beat_date(
            self,
            the_actor: Actor,
            date: datetime,
            locator: Target
    ):
        the_actor.attempts_to(
            Enter.the_text(date.strftime(self.DATE_FMT)).into_the(locator),
            Click.on_the(AssetListGamePage.BEAT_MODAL_HEADER)  # Close the date picker
        )

    @staticmethod
    def set_beat_name(
            the_actor: Actor,
            name: str
    ):
        the_actor.attempts_to(
            Enter.the_text(name).into_the(AssetListGamePage.BEAT_MODAL_NAME_INPUT)
        )

    @staticmethod
    def set_beat_phase(
            the_actor: Actor,
            phase: str
    ):
        the_actor.attempts_to(
            Enter.the_text(phase).into_the(AssetListGamePage.BEAT_MODAL_PHASE_DROPDOWN)
        )

    def set_beat_start_date(
            self,
            the_actor: Actor,
            start_date: datetime
    ):
        self.set_beat_date(the_actor, start_date, AssetListGamePage.BEAT_MODAL_START_DATE_INPUT)

    def set_beat_end_date(
            self,
            the_actor: Actor,
            end_date: datetime
    ):
        self.set_beat_date(the_actor, end_date, AssetListGamePage.BEAT_MODAL_START_DATE_INPUT)

    @staticmethod
    def set_beat_evergreen(
            the_actor: Actor,
            is_evergreen: bool
    ):
        evergreen_element = AssetListGamePage.BEAT_MODAL_IS_EVERGREEN_FILL.found_by(the_actor)
        actual_is_evergreen = evergreen_element.get_attribute("fill") is not None
        if actual_is_evergreen != is_evergreen:
            the_actor.attempts_to(
                Click.on_the(AssetListGamePage.BEAT_MODAL_IS_EVERGREEN_CHECKBOX)
            )
