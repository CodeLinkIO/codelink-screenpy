from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.actions import Clear, Wait, Enter, Click

from actions import WaitClick
from ui import AssetListGamePage


class SetDefaultLocales:

    def __init__(self, *locales) -> None:
        self.locales = locales

    @beat("{} sets default Youtube locales with '{locales}'.")
    def perform_as(self, the_actor: Actor) -> None:
        the_actor.attempts_to(
            WaitClick(AssetListGamePage.SET_DEFAULT_LOCALES_BUTTON)
        )
        for locale in self.locales:
            search_target = AssetListGamePage.SET_DEFAULT_LOCALES_MODAL_SEARCH_INPUT
            the_actor.attempts_to(
                Wait.for_the(search_target),
                Clear.the_text_from_the(search_target),
                Enter.the_text(locale).into_the(search_target),
                WaitClick(AssetListGamePage.SET_DEFAULT_LOCALES_MODAL_LOCALE_CHECKBOX),
                Click.on_the(AssetListGamePage.SET_DEFAULT_LOCALES_MODAL_CLOSE_BUTTON)
            )
