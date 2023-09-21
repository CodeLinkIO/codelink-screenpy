from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.actions import Click, Wait

from actions import WaitEnter
from ui import YoutubeHubPage
from .base_tasks import BaseTasks


class CreateNewVersionAsset(BaseTasks):

    def __init__(
            self,
            locale: str,
            version_name: str = None,
            aspect_ratio: str = None,
            channel: str = None
    ):
        self.version_name = version_name
        self.locale = locale
        self.aspect_ratio = aspect_ratio
        self.channel = channel

    @beat("{} creates new version asset.")
    def perform_as(self, the_actor: Actor) -> None:
        if self.version_name:
            the_actor.attempts_to(
                WaitEnter(YoutubeHubPage.CREATE_NEW_VERSION_ASSET_DIALOG_VERSION_NAME_INPUT, self.version_name)
            )
        if self.aspect_ratio:
            self.select_aspect_ratio(the_actor, self.aspect_ratio)
        self.select_locale(the_actor, self.locale)
        if self.channel:
            self.select_channel(the_actor, self.channel)
        the_actor.attempts_to(
            Click.on_the(YoutubeHubPage.CREATE_NEW_VERSION_ASSET_DIALOG_CREATE_NEW_VERSION_BUTTON),
            Wait.for_the(YoutubeHubPage.SMALL_LOADING_ICON).to_disappear()
        )
