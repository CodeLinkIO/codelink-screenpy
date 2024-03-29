from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.actions import Click

from ui.components import ToastMessageAlert


class CloseToastMessage:

    @beat("{} closes toast message.")
    def perform_as(self, the_actor: Actor) -> None:
        the_actor.attempts_to(
            Click.on_the(ToastMessageAlert.CLOSE_ICON)
        )
