from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.actions import Click, Wait

from actions import WaitClick, WaitEnter
from ui import YoutubeHubPage


class ExtractYouTubeMetadata:

    def __init__(
            self,
            video_id: str
    ):
        self.video_id = video_id

    @beat("{} extract YouTube metadata.")
    def perform_as(self, the_actor: Actor) -> None:
        the_actor.attempts_to(
            WaitEnter(YoutubeHubPage.EXTRACT_YOUTUBE_METADATA_DIALOG_YOUTUBE_ID_INPUT, self.video_id),
            Click.on_the(YoutubeHubPage.EXTRACT_YOUTUBE_METADATA_DIALOG_EXTRACT_METADATA_BUTTON),
            Wait.for_the(YoutubeHubPage.SMALL_LOADING_ICON).to_disappear()
        )
