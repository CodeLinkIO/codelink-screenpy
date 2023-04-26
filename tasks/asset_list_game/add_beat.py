from datetime import datetime

from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.actions import Enter, Wait, Click

from actions import WaitClick
from ui import AssetListGamePage
from .base_tasks import BaseTasks


class AddBeat(BaseTasks):

    def __init__(
            self,
            name: str,
            phase: str,
            start_date: datetime = None,
            end_date: datetime = None,
            is_evergreen: bool = False
    ):
        self.name = name
        self.phase = phase
        self.start_date = start_date
        self.end_date = end_date
        self.is_evergreen = is_evergreen

    @beat("{} adds beat with name '{name}'.")
    def perform_as(self, the_actor: Actor) -> None:
        the_actor.attempts_to(
            WaitClick(AssetListGamePage.ADD_BEAT_BUTTON),
            Wait.for_the(AssetListGamePage.BEAT_MODAL_HEADER),
            Enter.the_text(self.name).into_the(AssetListGamePage.BEAT_MODAL_NAME_INPUT),
            Enter.the_text(self.phase).into_the(AssetListGamePage.BEAT_MODAL_PHASE_DROPDOWN),
            Click.on_the(AssetListGamePage.BEAT_MODAL_HEADER)
        )
        if self.start_date:
            self.set_beat_start_date(the_actor, self.start_date)
        if self.end_date:
            self.set_beat_end_date(the_actor, self.end_date)
        self.set_beat_evergreen(the_actor, self.is_evergreen)
        the_actor.attempts_to(
            Click.on_the(AssetListGamePage.BEAT_MODAL_CREATE_BUTTON)
        )
