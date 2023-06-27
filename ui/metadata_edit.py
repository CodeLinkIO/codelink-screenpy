from screenpy_selenium import Target

from ui.base.base_page import BasePage


class MetadataEditPage(BasePage):

    # Header
    METADATA_CAPTURE_TAB = Target.the('Metadata Capture Tab').located_by("[class^='Header__Tabs'] div:first-child")
    ATTACH_THUMBNAILS_TAB = Target.the('Attach Thumbnails Tab').located_by("[class^='Header__Tabs'] div:last-child")
    PUBLISH_BUTTON = Target.the('Publish Button').located_by("//button[text()='PUBLISH']")

    # Metadata Capture
    ADD_NEW_LOCALE_BUTTON = Target.the('Add New Locale Button').located_by("[class*='AddNewLocaleButton'] button")
    ADD_NEW_LOCALES_BUTTON = Target.the('Add New Locales Button In Locale Dropdown List').located_by("//button[text()='ADD NEW LOCALES']")
    VALIDATE_BUTTON = Target.the('Validate Button').located_by("[class^=MetadataCaptureRow__RowWrapper]:first-child button[class*='ValidationButton']")
    SEARCH_LOCALE_INPUT = Target.the('Search Local Input').located_by("input[placeholder='Search']")
    ADD_TITLE_INPUT = Target.the('Add Title Input').located_by("[class^=MetadataCaptureRow__RowWrapper]:first-child textarea[placeholder='+ Add Title']")
    ADD_DESCRIPTION_INPUT = Target.the('Add Description Input').located_by("[class^=MetadataCaptureRow__RowWrapper]:first-child textarea[placeholder='+ Add Description']")
    ADD_TAGS_INPUT = Target.the('Add Tags Input').located_by("[class^=MetadataCaptureRow__RowWrapper]:first-child [contenteditable='true']")

    # Attach Thumbnails
    ADD_EDIT_MASTER_THUMBNAIL_BUTTON = Target.the('Add/Edit Master Thumbnail Button').located_by("//button[text()='ADD/EDIT MASTER THUMBNAIL ']")
    UPLOAD_THUMBNAIL_DROPZONE = Target.the('Upload Thumbnail Dropzone').located_by("[class^=Dropzone__Wrapper]")
    UPLOAD_MASTER_THUMBNAIL_INPUT = Target.the('Upload Master Thumbnail Input').located_by("[class^=Modal__Overlay] input[type=file]")
    UPLOAD_VERSION_THUMBNAIL_INPUT = Target.the('Upload Version Thumbnail Input').located_by("[class^=Dropzone__DropInput] input[type=file]")
    THUMBNAIL_IMAGE_PREVIEW = Target.the('Thumbnail Image Preview').located_by("[class^=SelectableImage]")
    ADD_EDIT_MASTER_THUMBNAIL_MODAL_DONE_BUTTON = Target.the('Done Button On Add/Edit Master Thumbnail Modal').located_by("[class^=Modal__Buttons] [class^=Button]")
    VERSION_THUMBNAIL_TABLE_THUMBNAIL_STATUS = Target.the('Thumbnail Status Columns').located_by("[class^=Modal__Buttons] [class^=Button]")
    EXPAND_VERSION_ASSET_ROW_ICON = Target.the('Expand Version Asset Row Icon').located_by("[class^='VersionAsset__VersionWrapper']:first-child [class^='VersionAsset__Header'] svg")
    USE_VERSION_THUMBNAIL_TOGGLE = Target.the('Use Version Thumbnail Toggle').located_by("[class^='VersionAsset__VersionWrapper']:first-child [class='slider round']")

    def __init__(self, url):
        super().__init__(url)

    @staticmethod
    def get_value_in_locale_dropdown_list(keyword: str) -> Target:
        return Target.the(f'"{keyword}" Value In Locale Dropdown List').located_by(f"//*[contains(@class,'LocaleLabel') and contains(text(), '{keyword}')]")
