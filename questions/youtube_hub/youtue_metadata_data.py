from screenpy import Actor
from screenpy.actions import MakeNote
from screenpy.directions import noted_under
from screenpy.pacing import beat

from questions.base_questions import BaseQuestions
from questions.helpers.string_helpers import ReplaceStringUsingRegexp
from ui.youtube_hub import YoutubeHubPage


class YouTubeMetadataData(BaseQuestions):

    @beat('{} examines the data on Extract YouTube Metadata Dialog')
    def answered_by(self, the_actor: Actor):
        headers = self.get_texts(the_actor, YoutubeHubPage.EXTRACT_YOUTUBE_METADATA_DIALOG_TABLE_HEADER)
        the_actor.attempts_to(
            MakeNote.of_the(
                ReplaceStringUsingRegexp(
                    self.get_text(the_actor, YoutubeHubPage.EXTRACT_YOUTUBE_METADATA_DIALOG_DESCRIPTION),
                    "\n|\n\n|\xa0"
                )
            ).as_("description"),
        )
        data = [
            self.get_text(the_actor, YoutubeHubPage.EXTRACT_YOUTUBE_METADATA_DIALOG_VIDEO_TITLE),
            noted_under("description"),
            self.get_texts(the_actor, YoutubeHubPage.EXTRACT_YOUTUBE_METADATA_DIALOG_SEARCH_TAGS),
            YoutubeHubPage.EXTRACT_YOUTUBE_METADATA_DIALOG_THUMBNAIL.found_by(the_actor).get_attribute("src"),
            self.get_text(the_actor, YoutubeHubPage.EXTRACT_YOUTUBE_METADATA_DIALOG_YOUTUBE_PUBLISH),
            self.get_text(the_actor, YoutubeHubPage.EXTRACT_YOUTUBE_METADATA_DIALOG_CHANNEL)
        ]
        return dict(zip(headers, data))
