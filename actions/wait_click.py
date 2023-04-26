from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.actions import Click
from screenpy_selenium import Target

from actions.base_actions import BaseActions


class WaitClick(BaseActions):

    def __init__(self, target: Target):
        self.target = target

    @beat("{} waits and clicks on the {target}.")
    def perform_as(self, the_actor: Actor) -> None:
        self.wait_for_target_to_perform_action(
            the_actor,
            self.target,
            Click.on_the(self.target)
        )
