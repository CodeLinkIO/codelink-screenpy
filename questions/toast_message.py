from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.actions import Wait
from screenpy_selenium.questions import Text

from ui.components import ToastMessageAlert


class ToastMessage:

    @beat('{} examines the toast message.')
    def answered_by(self, the_actor: Actor):
        the_actor.attempts_to(
            Wait.for_the(ToastMessageAlert.TOAST_MESSAGE)
        )
        return Text.of(ToastMessageAlert.TOAST_MESSAGE).answered_by(the_actor)
