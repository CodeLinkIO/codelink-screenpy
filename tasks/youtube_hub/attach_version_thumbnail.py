from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.actions import Click, Wait

from actions import WaitClick
from ui import MetadataEditPage
from .base_tasks import BaseTasks


class AttachVersionThumbnail(BaseTasks):

    def __init__(
            self,
            thumbnail_file: str,
    ):
        self.thumbnail_file = thumbnail_file

    @beat("{} attaches version thumbnail image and publish.")
    def perform_as(self, the_actor: Actor) -> None:
        the_actor.attempts_to(
            Click.on_the(MetadataEditPage.EXPAND_VERSION_ASSET_ROW_ICON),
            WaitClick(MetadataEditPage.USE_VERSION_THUMBNAIL_TOGGLE),
            Wait.for_the(MetadataEditPage.UPLOAD_THUMBNAIL_DROPZONE)
        )
        MetadataEditPage.UPLOAD_VERSION_THUMBNAIL_INPUT.found_by(the_actor).send_keys(self.thumbnail_file),
        the_actor.attempts_to(
            Wait.for_the(MetadataEditPage.SMALL_LOADING_ICON).to_disappear(),
            Wait.for_the(MetadataEditPage.THUMBNAIL_IMAGE_PREVIEW)
        )
