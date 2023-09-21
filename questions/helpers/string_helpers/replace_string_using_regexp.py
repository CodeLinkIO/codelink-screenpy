import re

from screenpy import Actor
from screenpy.actions import See
from screenpy.pacing import beat
from screenpy.resolutions import GreaterThan


class ReplaceStringUsingRegexp:

    def __init__(
            self,
            text: str,
            pattern: str
    ) -> None:
        self.text = text
        self.pattern = pattern

    @beat("{} examines the text after replaced with pattern '{pattern}' from the original text '{text}'.")
    def answered_by(self, the_actor: Actor) -> str:
        the_actor.should(See.the(len(self.text), GreaterThan(0)))
        return " ".join([x for x in re.split(rf'{self.pattern}', self.text) if len(x) > 0])
