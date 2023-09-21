from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.actions import Click, Wait

from ui import YoutubeHubPage
from .base_tasks import BaseTasks


class ImportYouTubeMetadata(BaseTasks):

    def __init__(
            self,
            locale: str,
            aspect_ratio: str = None,
            channel: str = None
    ):
        self.locale = locale
        self.aspect_ratio = aspect_ratio
        self.channel = channel

    @beat("{} imports YouTube metadata.")
    def perform_as(self, the_actor: Actor) -> None:
        if self.aspect_ratio:
            self.select_aspect_ratio(the_actor, self.aspect_ratio)
        self.select_locale(the_actor, self.locale)
        if self.channel:
            self.select_channel(the_actor, self.channel)
        the_actor.attempts_to(
            Click.on_the(YoutubeHubPage.CREATE_NEW_VERSION_ASSET_DIALOG_IMPORT_YOUTUBE_METADATA_BUTTON),
            Wait.for_the(YoutubeHubPage.SMALL_LOADING_ICON).to_disappear()
        )
