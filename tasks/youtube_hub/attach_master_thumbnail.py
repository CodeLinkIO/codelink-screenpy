from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.actions import Click, Wait

from ui import MetadataEditPage
from .base_tasks import BaseTasks


class AttachMasterThumbnail(BaseTasks):

    def __init__(
            self,
            thumbnail_file: str,
    ):
        self.thumbnail_file = thumbnail_file

    @beat("{} attaches master thumbnail image and publish.")
    def perform_as(self, the_actor: Actor) -> None:
        the_actor.attempts_to(
            Click.on_the(MetadataEditPage.ATTACH_THUMBNAILS_TAB),
            Click.on_the(MetadataEditPage.ADD_EDIT_MASTER_THUMBNAIL_BUTTON),
            Wait.for_the(MetadataEditPage.ADD_EDIT_MASTER_THUMBNAIL_MODAL_DONE_BUTTON),
        )
        MetadataEditPage.UPLOAD_MASTER_THUMBNAIL_INPUT.found_by(the_actor).send_keys(self.thumbnail_file)
        the_actor.attempts_to(
            Wait.for_the(MetadataEditPage.SMALL_LOADING_ICON).to_disappear(),
            Wait.for_the(MetadataEditPage.THUMBNAIL_IMAGE_PREVIEW),
            Click.on_the(MetadataEditPage.ADD_EDIT_MASTER_THUMBNAIL_MODAL_DONE_BUTTON)
        )
