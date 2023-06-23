from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.actions import Click, Wait, Enter

from actions import WaitEnter, WaitClick
from ui import YoutubeHubPage


class BaseTasks:

    @staticmethod
    def select_value_in_dropdown_on_dialog(the_actor: Actor, keyword: str):
        the_actor.attempts_to(
            WaitClick(YoutubeHubPage.CREATE_NEW_VERSION_ASSET_DIALOG_DROPDOWN_SEARCH_INPUT),
            Enter.the_text(keyword).into_the(YoutubeHubPage.CREATE_NEW_VERSION_ASSET_DIALOG_DROPDOWN_SEARCH_INPUT),
            WaitClick(YoutubeHubPage.get_value_in_dropdown_list(keyword)),
            Wait.for_the(YoutubeHubPage.CREATE_NEW_VERSION_ASSET_DIALOG_DROPDOWN_SEARCH_INPUT).to_disappear()
        )

    def select_locale(self, the_actor: Actor, locale: str):
        the_actor.attempts_to(
            Click.on_the(YoutubeHubPage.CREATE_NEW_VERSION_ASSET_DIALOG_LOCALE_DROPDOWN)
        )
        self.select_value_in_dropdown_on_dialog(the_actor, locale)

    def select_aspect_ratio(self, the_actor: Actor, aspect_ratio: str):
        the_actor.attempts_to(
            Click.on_the(YoutubeHubPage.CREATE_NEW_VERSION_ASSET_DIALOG_ASPECT_RATIO_DROPDOWN)
        )
        self.select_value_in_dropdown_on_dialog(the_actor, aspect_ratio)

    def select_channel(self, the_actor: Actor, channel: str):
        the_actor.attempts_to(
            Click.on_the(YoutubeHubPage.CREATE_NEW_VERSION_ASSET_DIALOG_CHANNEL_DROPDOWN)
        )
        self.select_value_in_dropdown_on_dialog(the_actor, channel)
