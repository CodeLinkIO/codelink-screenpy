import typing

from screenpy import Actor
from screenpy_selenium import Target


class BaseQuestions:

    @staticmethod
    def get_text(
            the_actor: Actor,
            target: Target
    ) -> str:
        return target.found_by(the_actor).text

    @staticmethod
    def get_texts(
            the_actor: Actor,
            target: Target
    ) -> typing.List[str]:
        return [element.text for element in target.all_found_by(the_actor)]
