from retry import retry
from screenpy_selenium import Target
from screenpy_selenium.actions import Chain, Click, Hover, Wait
from selenium.common import StaleElementReferenceException

from actions import WaitClick, WaitEnter
from screenpy import Actor
from screenpy.pacing import beat
from ui import YoutubePublishPage

from .base_tasks import BaseTasks


class PublishYoutubeVersion(BaseTasks):

    def __init__(
            self,
            file_name: str,
            metadata_locale: str = None,
            youtube_channels: str = None,
    ):
        self.file_name = file_name
        self.metadata_locale = metadata_locale
        self.youtube_channels = youtube_channels

    @staticmethod
    @retry(StaleElementReferenceException, tries=5, delay=1)
    def expand_dropdown(the_actor: Actor, target: Target):
        the_actor.attempts_to(
            Chain(
                Hover.on_the(target),
                Click.on_the(target)
            ),
            Wait.for_the(YoutubePublishPage.SEARCH_INPUT)
        )

    def set_metadata_locale(self, the_actor: Actor):
        self.expand_dropdown(the_actor, YoutubePublishPage.get_metadata_locale_button_by_file_name(self.file_name))
        the_actor.attempts_to(
            WaitEnter(YoutubePublishPage.SEARCH_INPUT, self.metadata_locale),
            WaitClick(YoutubePublishPage.get_value_in_dropdown_list(self.metadata_locale)),
            Wait.for_the(YoutubePublishPage.get_metadata_locale_value_selected(self.file_name, self.metadata_locale))
        )

    def set_youtube_channels(self, the_actor: Actor):
        self.expand_dropdown(the_actor, YoutubePublishPage.get_youtube_channels_button_by_file_name(self.file_name))
        the_actor.attempts_to(
            WaitEnter(YoutubePublishPage.SEARCH_INPUT, self.youtube_channels),
            WaitClick(YoutubePublishPage.get_value_in_dropdown_list(self.youtube_channels)),
            Wait.for_the(YoutubePublishPage.get_youtube_channels_value_selected(self.file_name, self.youtube_channels))
        )

    @beat("{} publishes YouTube version.")
    def perform_as(self, the_actor: Actor) -> None:
        the_actor.attempts_to(
            Wait.for_the(YoutubePublishPage.VIDEO_THUMBNAIL)
        )
        self.metadata_locale and self.set_metadata_locale(the_actor)
        self.youtube_channels and self.set_youtube_channels(the_actor)
        the_actor.attempts_to(
            Click.on_the(YoutubePublishPage.VERSION_CHECKBOX),
            Click.on_the(YoutubePublishPage.PUBLISH_SELECTED_BUTTON),
            WaitClick(YoutubePublishPage.PUBLISH_VIDEOS_CONFIRMATION_MODAL_PUBLISH_BUTTON),
            Wait(30).seconds_for_the(YoutubePublishPage.SMALL_LOADING_ICON).to_disappear()
        )
