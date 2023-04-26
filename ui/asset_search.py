from screenpy_selenium import Target

from ui.base.base_page import BasePage


class AssetSearchPage(BasePage):

    # Search Bar Header
    SEARCH_FOR_ASSETS_DROPDOWN = Target.the('Search For Assets Dropdown').located_by("#asset_selector")
    SEARCH_ALL_TITLES_INPUT = Target.the('Search All Titles Input').located_by("input[class^='SearchFilterTags__Input']")
    SEARCH_ALL_TITLES_DROPDOWN = Target.the('Search All Titles Filter Dropdown').located_by("[class^='SearchFilterTags__FilterMenu']")
    SEARCH_ALL_TITLES_ICON = Target.the('Search All Titles Icon').located_by("button[class^='SearchFilterTags__SearchButton']")

    # Filter Panel
    FIND_TAGS_SEARCH_INPUT = Target.the('Find Tags Search Input').located_by("input[class^='SearchInput']")
    FIND_TAGS_SEARCH_ICON = Target.the('Find Tags Search Icon').located_by("div[class^='SearchInput'] svg")

    # Filter Row
    CLEAR_ALL_FILTERS_LINK = Target.the('Clear All Filters Link').located_by("[class*=FilterTagList__ClearLink]")
    NUM_ASSETS_AVAILABLE_LABEL = Target.the('Number Of Assets Available Label').located_by("[class*=FilterTagList__HeadButton]")
    VIEW_ASSETS_LINK = Target.the('View Assets Link').located_by("[class='clickable fetch']")

    # Results Table
    COLUMN_HEADER = Target.the('Column Header').located_by("sortableColumn")
    DATA_ROW = Target.the('Column Header').located_by("[class*='DefaultTableRowRenderer']")

    def __init__(self, url):
        super().__init__(url)
