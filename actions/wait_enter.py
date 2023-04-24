from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.actions import Enter
from screenpy_selenium import Target

from actions.base_actions import BaseActions


class WaitEnter(BaseActions):

    def __init__(self, target: Target, text: str):
        self.target = target
        self.text = text

    @beat('{} waits and enters "{text}" into the {target}.')
    def perform_as(self, the_actor: Actor) -> None:
        self.wait_for_target_to_perform_action(
            the_actor,
            self.target,
            Enter.the_text(self.text).into_the(self.target)
        )
