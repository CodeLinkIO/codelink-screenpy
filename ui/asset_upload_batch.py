from screenpy_selenium import Target

from ui.base.base_page import BasePage


class AssetUploadBatchPage(BasePage):

    # Header
    BACK_LINK = Target.the('Back To Asset Upload Link').located_by("[class^='BatchPage__BackLink']")
    HEADER_LABEL = Target.the('Header Label').located_by("[class^='HeadingBreadcrumb']")
    ASSET_ID_LABEL = Target.the('Asset ID Label').located_by("[class^='BatchPage__AssetId']")

    # Search And Actions Tab
    SEARCH_INPUT_ASSET_NAME = Target.the('Search Input Asset Name').located_by("input[type='search']")
    DELETE_SELECTED_ROWS_BUTTON = Target.the('Delete Selected Rows Button').located_by("//button[text()='DELETE SELECTED ROWS']")
    RUN_AUTO_TAGGING_BUTTON = Target.the('Run Auto Tagging Button').located_by("//button[text()='RUN AUTO TAGGING']")
    ADD_EXTRA_METADATA_BUTTON = Target.the('Add Extra Metadata Button').located_by("//button[text()='ADD EXTRA METADATA']")
    UPLOAD_FOLDER_BUTTON = Target.the('Upload Folder Button').located_by("//button[text()='UPLOAD FOLDER']")
    UPLOAD_FILES_BUTTON = Target.the('Upload Files Button').located_by("//button[text()='UPLOAD FILES']")

    # Upload Table
    UPLOAD_AREA = Target.the('File Input').located_by("[class^='DropArea__FileSelect']")
    FILE_INPUT = Target.the('File Input').located_by("[class^='DropArea'] [class^='FileSelector']:nth-of-type(1) input")
    FOLDER_INPUT = Target.the('Folder Input').located_by("[class^='DropArea'] [class^='FileSelector']:nth-of-type(2) input")

    def __init__(self, url):
        super().__init__(url)
