from screenpy_selenium import Target

from ui.base.base_page import BasePage


class AssetUploadPage(BasePage):

    # Search Section In The Header
    SEARCH_INPUT_HEADER = Target.the('Search Input In Header').located_by("input[class^='SearchInput']")
    SEARCH_ICON_HEADER = Target.the('Search Icon In Header').located_by("[class^='SearchInput__Button']")

    # Search Section In My Uploads Tab
    SEARCH_INPUT_MY_UPLOADS = Target.the('Search Input In My Upload Tab').located_by("input[class^='SearchBatchInput']")
    SEARCH_ICON_MY_UPLOADS = Target.the('Search Icon In My Upload Tab').located_by("[class^='SearchBatchInput__SearchIcon']")
    NO_BATCHES_FOUND = Target.the('No Batches Found Description').located_by("[class^='BatchList__Empty']")

    # Create New Batch Modal
    NEW_BATCH_MODAL_HEADER = Target.the('Create New Batch Header').located_by("[class^='Modal__Heading']")
    NEW_BATCH_MODAL_BATCH_NAME_INPUT = Target.the('Batch Name Input On Create New Batch Modal').located_by("[class^='Modal__Content'] input[class^='InputModal']")
    NEW_BATCH_MODAL_CANCEL_BUTTON = Target.the('Cancel Button On Create New Batch Modal').located_by("[class^='Modal__Buttons'] [class^='CancelButton']")
    NEW_BATCH_MODAL_CREATE_BATCH_BUTTON = Target.the('Create Batch Button On Create New Batch Modal').located_by("[class^='Modal__Buttons'] [class^='Button']")

    # No Asset Found Modal
    NO_ASSET_FOUND_HEADER = Target.the('No Asset Found Header').located_by("[class^='BaseModal__HeadingContent']")
    NO_ASSET_FOUND_DESCRIPTION = Target.the('Description On No Asset Found Modal').located_by("[class^='BaseModal__Content']")
    NO_ASSET_FOUND_CLOSE_BUTTON = Target.the('Close Button On No Asset Found Modal').located_by("[class^='BaseButton__Button']")

    def __init__(self, url):
        super().__init__(url)
