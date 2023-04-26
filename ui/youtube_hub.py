from screenpy_selenium import Target

from ui.base.base_page import BasePage


class YoutubeHubPage(BasePage):

    # Search Bar Header
    SEARCH_MASTER_ASSETS_ID_INPUT = Target.the('Master Asset ID Input').located_by("[class^='YoutubeLanding__EmptyDashboard'] input[class^='MasterIdInput__Input']")
    SEARCH_MASTER_ASSETS_ID_ICON = Target.the('Master Asset ID Icon').located_by("[class^='YoutubeLanding__EmptyDashboard'] [class^='MasterIdInput__Button']")

    # Filter Panel
    SEARCH_MASTER_ASSETS_ID_INPUT_FILTER_PANEL = Target.the('Master Asset ID Input On The Filter Panel').located_by("[class^='Sidebar__MasterInputWrapper'] input[class^='MasterIdInput']")
    SEARCH_MASTER_ASSETS_ID_ICON_FILTER_PANEL = Target.the('Master Asset ID Icon On The Filter Panel').located_by("[class^='Sidebar__MasterInputWrapper'] [class^='MasterIdInput__Button']")
    FIND_TAGS_SEARCH_INPUT = Target.the('Find Tags Search Input').located_by("input[class^='GameSearchBar']")
    FIND_TAGS_SEARCH_ICON = Target.the('Find Tags Search Icon').located_by("div[class^='SearchInput'] svg")

    def __init__(self, url):
        super().__init__(url)
