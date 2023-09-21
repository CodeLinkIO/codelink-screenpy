import time

from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.actions import Click, Wait, Enter
from selenium.webdriver import Keys

from actions import WaitClick
from ui import MetadataEditPage
from .base_tasks import BaseTasks


class EditMetadata(BaseTasks):

    def __init__(
            self,
            locale: str,
            title: str,
            description: str,
            tags: list
    ):
        self.title = title
        self.description = description
        self.locale = locale
        self.tags = tags

    def add_locale(self, the_actor: Actor):
        the_actor.attempts_to(
            WaitClick(MetadataEditPage.ADD_NEW_LOCALE_BUTTON),
            WaitClick(MetadataEditPage.SEARCH_LOCALE_INPUT),
            Enter.the_text(self.locale).into_the(MetadataEditPage.SEARCH_LOCALE_INPUT),
            WaitClick(MetadataEditPage.get_value_in_locale_dropdown_list(self.locale)),
            Click.on_the(MetadataEditPage.ADD_NEW_LOCALES_BUTTON),
            Wait.for_the(MetadataEditPage.ADD_NEW_LOCALES_BUTTON).to_disappear()
        )

    @staticmethod
    def focus_out(the_actor: Actor):
        the_actor.attempts_to(
            Click.on_the(MetadataEditPage.METADATA_CAPTURE_TAB)
        )

    def add_title(self, the_actor: Actor):
        the_actor.attempts_to(
            WaitClick(MetadataEditPage.ADD_TITLE_INPUT),
            Enter.the_text(self.title).into_the(MetadataEditPage.ADD_TITLE_INPUT),
            Click.on_the(MetadataEditPage.METADATA_CAPTURE_TAB)
        )

    def add_description(self, the_actor: Actor):
        the_actor.attempts_to(
            WaitClick(MetadataEditPage.ADD_DESCRIPTION_INPUT),
            Enter.the_text(self.description).into_the(MetadataEditPage.ADD_DESCRIPTION_INPUT),
            Click.on_the(MetadataEditPage.METADATA_CAPTURE_TAB)
        )

    def add_tags(self, the_actor: Actor):
        the_actor.attempts_to(
            WaitClick(MetadataEditPage.ADD_TAGS_INPUT)
        )
        for tag in self.tags:
            the_actor.attempts_to(
                Enter.the_text(tag).into_the(MetadataEditPage.ADD_TAGS_INPUT).then_hit(Keys.ENTER)
            )
        the_actor.attempts_to(
            Click.on_the(MetadataEditPage.METADATA_CAPTURE_TAB)
        )

    @staticmethod
    def wait_for_validate_button_enabled(the_actor: Actor, timeout: int = 5):

        def _is_disabled():
            attributes = MetadataEditPage.VALIDATE_BUTTON.found_by(the_actor).get_attribute('outerHTML')
            return "disabled" in attributes
        end_time = time.time() + timeout
        while time.time() <= end_time:
            if not _is_disabled():
                return
            time.sleep(0.5)
        raise TimeoutError(f"Validate button is not enabled after waiting {timeout} seconds.")

    @beat("{} edits metadata.")
    def perform_as(self, the_actor: Actor) -> None:
        the_actor.attempts_to(
            WaitClick(MetadataEditPage.METADATA_CAPTURE_TAB)
        )
        self.add_locale(the_actor)
        self.add_title(the_actor)
        self.add_description(the_actor)
        self.add_tags(the_actor)
        self.wait_for_validate_button_enabled(the_actor)
        the_actor.attempts_to(
            Click.on_the(MetadataEditPage.VALIDATE_BUTTON),
            Wait.for_the(MetadataEditPage.SMALL_LOADING_ICON).to_disappear()
        )
