from datetime import datetime
from retry import retry

from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.actions import Wait, Click, Chain, Hover
from selenium.common import StaleElementReferenceException

from ui import AssetListGamePage
from .base_tasks import BaseTasks


class EditBeat(BaseTasks):

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
            self.set_beat_name(the_actor, self.name)
        if self.phase:
            self.set_beat_phase(the_actor, self.phase)
        if self.start_date:
            self.set_beat_start_date(the_actor, self.start_date)
        if self.end_date:
            self.set_beat_end_date(the_actor, self.end_date)
        self.set_beat_evergreen(the_actor, self.is_evergreen)
        the_actor.attempts_to(
            Click.on_the(AssetListGamePage.BEAT_MODAL_SAVE_BUTTON)
        )
