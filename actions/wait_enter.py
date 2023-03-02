from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.actions import Wait, Enter
from screenpy_selenium import Target


class WaitEnter:

    def __init__(self, target: Target, text: str):
        self.target = target
        self.text = text

    @beat('{} waits and enters "{text}" into the {target}.')
    def perform_as(self, the_actor: Actor) -> None:
        the_actor.attempts_to(
            Wait.for_the(self.target),
            Enter.the_text(self.text).into_the(self.target)
        )
