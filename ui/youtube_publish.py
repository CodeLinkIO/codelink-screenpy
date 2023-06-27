from screenpy_selenium import Target

from ui.base.base_page import BasePage


class YoutubePublishPage(BasePage):

    SMALL_LOADING_ICON = Target.the('Small Loading Icon').located_by("[class^='SmallLoader']")

    # Header
    PUBLISH_SELECTED_BUTTON = Target.the('Publish Selected Button').located_by("//button[contains(text(), 'PUBLISH SELECTED')]")
    ATTACH_THUMBNAILS_TAB = Target.the('Attach Thumbnails Tab').located_by("//div[text()='Attach Thumbnails']")
    PUBLISH_BUTTON = Target.the('Publish Button').located_by("//button[text()='PUBLISH']")

    # YouTube Version Row
    VERSION_CHECKBOX = Target.the('Version Checkbox').located_by("(//div[contains(@class, 'VersionRow__RowWrapper')])[1]//input[@type='checkbox']")
    VIDEO_THUMBNAIL = Target.the('Video Thumbnail').located_by("[class^='SelectableVideo__Thumbnail']")
    METADATA_LOCALE_DROPDOWN = Target.the('Metadata Locale Dropdown').located_by("//span[text()='Select locale']/..")
    YOUTUBE_CHANNELS_DROPDOWN = Target.the('YouTube Channels Dropdown').located_by("//span[text()='Select locale']/..")
    SEARCH_INPUT = Target.the('Search Input In Dropdown List').located_by("input[placeholder='Search']")

    # Publish Videos Confirmation Modal
    PUBLISH_VIDEOS_CONFIRMATION_MODAL_PUBLISH_BUTTON = Target.the('Publish Button On Publish Videos Confirmation Modal').located_by("//div[contains(@class, 'Modal__Overlay')]//button[contains(text(), 'PUBLISH')]")

    def __init__(self, url):
        super().__init__(url)

    @staticmethod
    def get_value_in_dropdown_list(keyword: str) -> Target:
        return Target.the(f'"{keyword}" Value In Dropdown List').located_by(f"//li[contains(text(), '{keyword}')]")

    @staticmethod
    def get_version_row_by_file_name(file_name: str) -> Target:
        return Target.the(f'Version Row With File Name "{file_name}"').located_by(
            f"//*[contains(@class,'VersionRow__FieldValue') and contains(text(), '{file_name}')]"
            f"/ancestor::div[contains(@class, 'VersionRow__RowWrapper')]"
        )

    @staticmethod
    def get_metadata_locale_button_by_file_name(file_name: str) -> Target:
        return Target.the(f'Button to Select Locale Of File Name "{file_name}"').located_by(
            f"//div[text()='{file_name}']/../..//../div[contains(@class,'VersionRow__InnerCell')][7]//button"
        )

    @staticmethod
    def get_metadata_locale_value_selected(file_name: str, value: str) -> Target:
        return Target.the(f'Selected Locale Value Of File Name "{file_name}"').located_by(
            f"//div[text()='{file_name}']/../..//../div[contains(@class,'VersionRow__InnerCell')][7]//span[text()='{value}']"
        )

    @staticmethod
    def get_youtube_channels_button_by_file_name(file_name: str) -> Target:
        return Target.the(f'Button to Select YouTube Channel Of File Name "{file_name}"').located_by(
            f"//div[text()='{file_name}']/../..//../div[contains(@class,'VersionRow__InnerCell')][8]//button"
        )

    @staticmethod
    def get_youtube_channels_value_selected(file_name: str, value: str) -> Target:
        return Target.the(f'Selected YouTube Channel Value Of File Name "{file_name}"').located_by(
            f"//div[text()='{file_name}']/../..//../div[contains(@class,'VersionRow__InnerCell')][8]//span[text()='{value}']"
        )
