from screenpy import Actor
from screenpy.protocols import Performable
from screenpy_selenium.actions import Wait
from screenpy_selenium import Target


class BaseActions:

    DEFAULT_TIMEOUT = 10

    def wait_for_target_to_perform_action(
            self,
            the_actor: Actor,
            target: Target,
            action: Performable
    ) -> None:
        the_actor.attempts_to(
            Wait(self.DEFAULT_TIMEOUT).second_for_the(target),
            action
        )
