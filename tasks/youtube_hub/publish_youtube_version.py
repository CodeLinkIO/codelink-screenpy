from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.actions import Click, Wait

from actions import WaitEnter, WaitClick
from ui import YoutubePublishPage
from .base_tasks import BaseTasks


class PublishYoutubeVersion(BaseTasks):

    def __init__(
            self,
            metadata_locale: str = None,
            youtube_channels: str = None,
    ):
        self.metadata_locale = metadata_locale
        self.youtube_channels = youtube_channels

    def set_metadata_locale(self, the_actor: Actor):
        the_actor.attempts_to(
            WaitClick(YoutubePublishPage.METADATA_LOCALE_DROPDOWN),
            WaitEnter(YoutubePublishPage.SEARCH_INPUT, self.metadata_locale),
            WaitClick(YoutubePublishPage.get_value_in_dropdown_list(self.metadata_locale))
        )

    def set_youtube_channels(self, the_actor: Actor):
        the_actor.attempts_to(
            WaitClick(YoutubePublishPage.YOUTUBE_CHANNELS_DROPDOWN),
            WaitEnter(YoutubePublishPage.SEARCH_INPUT, self.youtube_channels),
            WaitClick(YoutubePublishPage.get_value_in_dropdown_list(self.youtube_channels))
        )

    @beat("{} publishes YouTube version.")
    def perform_as(self, the_actor: Actor) -> None:
        self.metadata_locale and self.set_metadata_locale(the_actor)
        self.youtube_channels and self.set_youtube_channels(the_actor)
        the_actor.attempts_to(
            Click.on_the(YoutubePublishPage.VERSION_CHECKBOX),
            Click.on_the(YoutubePublishPage.PUBLISH_SELECTED_BUTTON),
            WaitClick(YoutubePublishPage.PUBLISH_VIDEOS_CONFIRMATION_MODAL_PUBLISH_BUTTON),
            Wait.for_the(YoutubePublishPage.SMALL_LOADING_ICON).to_disappear()
        )
