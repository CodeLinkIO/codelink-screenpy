from screenpy import Actor
from screenpy.pacing import beat

from questions.base_questions import BaseQuestions
from ui.metadata_edit import MetadataEditPage


class ThumbnailStatusData(BaseQuestions):

    @beat('{} examines the data on Thumbnail Status columns on Attach Thumbnails tab')
    def answered_by(self, the_actor: Actor):
        return self.get_texts(the_actor, MetadataEditPage.VERSION_THUMBNAIL_TABLE_THUMBNAIL_STATUS)
