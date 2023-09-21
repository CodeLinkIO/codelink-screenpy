from enum import Enum

from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.actions import Clear, Click, Enter, Wait

from actions import WaitClick
from ui import YoutubeHubPage


class SearchGameTitleStatus(Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'


class SearchGameTitleType(Enum):
    EA = 'ea'
    NON_EA = 'non_ea'


class SearchGameTitle:

    def __init__(
            self,
            keyword: str,
            status: SearchGameTitleStatus = None,
            title_type: SearchGameTitleType = None,
            expanded_all_items: bool = True
    ):
        self.keyword = keyword
        self.status = status
        self.type = title_type
        self.expanded_all_items = expanded_all_items
        self.filter_to_log = f" and {', '.join([fil.value + ' title filter' for fil in [self.status, self.type] if fil is not None])}"

    def enter_keyword(self, the_actor: Actor):
        locator = YoutubeHubPage.FIND_TITLE_SEARCH_INPUT
        the_actor.attempts_to(
            Wait.for_the(locator),
            Clear.the_text_from_the(locator),
            Enter.the_text(self.keyword).into_the(locator)
        )

    def filter_status(self, the_actor: Actor):
        if self.status == SearchGameTitleStatus.ACTIVE:
            the_actor.attempts_to(Click.on_the(YoutubeHubPage.FIND_TITLE_SEARCH_ACTIVE))
        else:
            the_actor.attempts_to(Click.on_the(YoutubeHubPage.FIND_TITLE_SEARCH_INACTIVE))

    def filter_type(self, the_actor: Actor):
        if self.type == SearchGameTitleType.EA:
            the_actor.attempts_to(Click.on_the(YoutubeHubPage.FIND_TITLE_SEARCH_EA))
        else:
            the_actor.attempts_to(Click.on_the(YoutubeHubPage.FIND_TITLE_SEARCH_NON_EA))

    @staticmethod
    def expand_all_items(the_actor: Actor):
        the_actor.attempts_to(
            WaitClick(YoutubeHubPage.SECOND_COLLAPSED_TITLE_HEADER),
            WaitClick(YoutubeHubPage.ALL_COLLAPSED_ITEM),
            Wait.for_the(YoutubeHubPage.LOADING_ICON).to_disappear()
        )

    @beat("{} searches for Game Title with keyword '{keyword}'{filter_to_log}.")
    def perform_as(self, the_actor: Actor) -> None:
        self.enter_keyword(the_actor)
        if self.status is not None:
            self.filter_status(the_actor)
        if self.type is not None:
            self.filter_type(the_actor)
        if self.expanded_all_items:
            self.expand_all_items(the_actor)
