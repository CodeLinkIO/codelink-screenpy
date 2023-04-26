from datetime import datetime

from screenpy_selenium import Target

from enums.search_non_game_asset_type import SearchNonGameAssetType
from ui.base.base_page import BasePage


class AssetListNonGamePage(BasePage):

    # Base Buttons
    SHARE_BUTTON = Target.the('Share Button').located_by("[class^='Header__ActionWrapper'] [class^='BaseButton__Button']:first-child")
    ADD_EDIT_ASSET_BUTTON = Target.the('Add / Edit Asset Button').located_by("[class^='Header__ActionWrapper'] [class^='BaseButton__Button']:last-child")
    SAVE_CHANGES_BUTTON = Target.the('Save Changes Button').located_by("[class^='Header__ActionWrapper'] [class^='BaseButton__Button']:first-child")
    CANCEL_BUTTON = Target.the('Cancel Button').located_by("[class^='Header__ActionWrapper'] [class^='BaseButton__Button']:last-child")
    MORE_FILTER_BUTTON = Target.the('More Filter Button').located_by("[class^='Header__FilterWrapper'] [class^='BaseButton__Button']")
    ADD_BUTTON = Target.the('Add Button').located_by("[class^='AssetList__ActionPanel'] [class^='BaseButton__Button']")

    # Search Section
    SEARCH_INPUT = Target.the('Search Input').located_by("input[class^='SearchInput']")

    # New Master Asset Section
    REMOVE_NEW_MASTER_ASSET_ICON = Target.the('Remove Icon On New Master Asset Row').located_by("[class^='nonGameTable__Row']:nth-of-type(2) [class^='ActionCell__StyledIcon']")
    GO_LIVE_DATE_NEW_MASTER_ASSET_FIELD = Target.the('Go Live Date Field On New Master Asset Row').located_by("[class^='nonGameTable__Row']:nth-of-type(2) [class^='Cell__CellWrapper']:nth-of-type(4) [class^='DateCell__Content']")
    BEAT_NEW_MASTER_ASSET_FIELD = Target.the('Beat Field On New Master Asset Row').located_by("[class^='nonGameTable__Row']:nth-of-type(2) [class^='Cell__CellWrapper']:nth-of-type(6) div[class^='SingleSelectCell']")
    ASSET_TYPE_NEW_MASTER_ASSET_FIELD = Target.the('Asset Type Field On New Master Asset Row').located_by("[class^='nonGameTable__Row']:nth-of-type(2) [class^='Cell__CellWrapper']:nth-of-type(7) div[class^='SingleSelectCell']")
    CONTENT_TYPE_NEW_MASTER_ASSET_FIELD = Target.the('Content Type Field On New Master Asset Row').located_by("[class^='nonGameTable__Row']:nth-of-type(2) [class^='Cell__CellWrapper']:nth-of-type(8) div[class^='SingleSelectCell']")
    ASSET_NAME_NEW_MASTER_ASSET_FIELD = Target.the('Asset Name Field On New Master Asset Row').located_by("[class^='nonGameTable__Row']:nth-of-type(2) [class^='Cell__CellWrapper']:nth-of-type(9) div[class^='InputCel']")
    ASSET_NAME_NEW_MASTER_ASSET_INPUT = Target.the('Asset Name Input On New Master Asset Row').located_by("input[class^='InputCell']")
    CATEGORY_NEW_MASTER_ASSET_FIELD = Target.the('Category Field On New Master Asset Row').located_by("[class^='nonGameTable__Row']:nth-of-type(2) [class^='Cell__CellWrapper']:nth-of-type(10) div[class^='SingleSelectCell']")
    SUB_CATEGORY_NEW_MASTER_ASSET_FIELD = Target.the('Sub Category Field On New Master Asset Row').located_by("[class^='nonGameTable__Row']:nth-of-type(2) [class^='Cell__CellWrapper']:nth-of-type(11) div[class^='SingleSelectCell']")
    PLANNED_CHANNELS_NEW_MASTER_ASSET_FIELD = Target.the('Planned Channels Field On New Master Asset Row').located_by("[class^='nonGameTable__Row']:nth-of-type(2) [class^='Cell__CellWrapper']:nth-of-type(12)")
    NOTES_NEW_MASTER_ASSET_FIELD = Target.the('Notes Field On New Master Asset Row').located_by("[class^='nonGameTable__Row']:nth-of-type(2) [data-for='global-tip']")
    NOTES_NEW_MASTER_ASSET_INPUT = Target.the('Notes Input On New Master Asset Row').located_by("textarea[class^='InputCell']")

    # Assets Table
    LOADING_ICON = Target.the('Loading Icon On Assets Table').located_by("[class^='Loader__Wrapper']")
    HEADER_ROW_ITEM = Target.the('Item On Header Row').located_by("[class^='nonGameTable__HeaderRow'] div div")
    ASSET_ROW = Target.the('Asset Row').located_by("[class^='nonGameTable__InnerList'] [class^='nonGameTable__Row']")
    PLANNED_CHANNELS_COLUMN_HEADER = Target.the('Planned Channels Column Header').located_by("//*[contains(@class,'nonGameTable__HeaderRow')]//*[text()='Planned Channels']")
    NOTES_COLUMN_HEADER = Target.the('Notes Column Header').located_by("[class^='nonGameTable__HeaderRow'] [role='columnheader']:last-child")
    SEARCH_INPUT_SELECT_DROPDOWN_LIST = Target.the('Search Input On Select Dropdown List').located_by("input[class^='SingleSelectList']")
    SEARCH_INPUT_MULTI_SELECT_DROPDOWN_LIST = Target.the('Search Input On Multi Select Dropdown List').located_by("input[class^='MultiSelectList']")

    # Confirmation Dialog
    CANCEL_BUTTON_CONFIRMATION_DIALOG = Target.the('Cancel Button On Confirmation Dialog').located_by("[class^='BaseModal__Overlay'] [class^='BaseButton__Button']:first-child")
    CONTINUE_BUTTON_CONFIRMATION_DIALOG = Target.the('Continue Button On Confirmation Dialog').located_by("[class^='BaseModal__Overlay'] [class^='BaseButton__Button']:last-child")

    def __init__(self, url):
        super().__init__(url)

    @staticmethod
    def get_go_live_date_picker(go_live_date: datetime) -> Target:
        go_live_date_str = go_live_date.strftime("%B %#d, %Y")
        return Target.the('Go Live Date On The Date Picker').located_by(f"[aria-label='{go_live_date_str}']")

    @staticmethod
    def get_search_select_dropdown_list_result(keyword: str) -> Target:
        return Target.the('Desired Result After Search On Select Dropdown List').located_by(
            f"//*[contains(@class,'SingleSelectList')]//*[text()='{keyword}']")

    @staticmethod
    def get_search_multi_select_dropdown_list_result(keyword: str) -> Target:
        return Target.the('Desired Result After Search On Multi Select Dropdown List').located_by(
            f"//*[contains(@class,'MultiSelectList')]//*[text()='{keyword}']")

    @staticmethod
    def get_search_suggestion(keyword: str, search_type: SearchNonGameAssetType) -> Target:
        return Target.the('Search Suggest Of Asset Name When Search Non Game Asset').located_by(
            f"//*[contains(@class,'SearchSuggestionPopup') and text()='{search_type.value}']"
            f"/following-sibling::div[@id='{keyword}']")
