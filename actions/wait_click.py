from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.actions import Wait, Click
from screenpy_selenium import Target


class WaitClick:

    def __init__(self, target: Target):
        self.target = target

    @beat("{} waits and clicks on the {target}.")
    def perform_as(self, the_actor: Actor) -> None:
        the_actor.attempts_to(
            Wait.for_the(self.target),
            Click.on_the(self.target)
        )
