from screenpy import Actor
from screenpy.pacing import beat

from questions.base_questions import BaseQuestions
from ui import YoutubePublishPage


class PublishedYoutubeVersionDisabled(BaseQuestions):

    def __init__(
            self,
            file_name: str = None
    ):
        self.file_name = file_name

    @beat('{} examines the YouTube version row published is disabled.')
    def answered_by(self, the_actor: Actor):
        version_row = YoutubePublishPage.get_version_row_by_file_name(self.file_name).all_found_by(the_actor)
        is_all_items_disabled = []
        for item in version_row:
            is_all_items_disabled.append("disabled" in item.get_attribute("outerHTML"))
        return all(is_all_items_disabled)
