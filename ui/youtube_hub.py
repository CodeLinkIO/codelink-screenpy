from screenpy_selenium import Target

from ui.base.base_page import BasePage


class YoutubeHubPage(BasePage):

    LOADING_ICON = Target.the('Loading Icon').located_by("Loader__Ring")
    SMALL_LOADING_ICON = Target.the('Small Loading Icon').located_by("[class^='SmallLoader']")
    ROW_TABLE = Target.the('Row On Table').located_by("[class='ReactVirtualized__Table__row']")

    # Search Bar Header
    SEARCH_MASTER_ASSET_ID_INPUT = Target.the('Master Asset ID Input').located_by("input[class^='MasterIdInput']")
    SEARCH_MASTER_ASSET_ID_ICON = Target.the('Master Asset ID Icon').located_by("[class^='MasterIdInput__Button']")

    # Filter Panel
    SEARCH_MASTER_ASSETS_ID_INPUT_FILTER_PANEL = Target.the('Master Asset ID Input On The Filter Panel').located_by("[class^='Sidebar__MasterInputWrapper'] input[class^='MasterIdInput']")
    SEARCH_MASTER_ASSETS_ID_ICON_FILTER_PANEL = Target.the('Master Asset ID Icon On The Filter Panel').located_by("[class^='Sidebar__MasterInputWrapper'] [class^='MasterIdInput__Button']")
    FIND_TITLE_SEARCH_INPUT = Target.the('Find Title Search Input').located_by("input[class^='GameSearchBar']")
    FIND_TITLE_SEARCH_ICON = Target.the('Find Title Search Icon').located_by("div[class^='SearchInput'] svg")
    FIND_TITLE_SEARCH_ALL = Target.the('Find Title Search All').located_by("//*[contains(@class,'GameFilters__FilterButton') and text()='All']")
    FIND_TITLE_SEARCH_ACTIVE = Target.the('Find Title Search Active').located_by("//*[contains(@class,'GameFilters__FilterButton') and text()='Active']")
    FIND_TITLE_SEARCH_INACTIVE = Target.the('Find Title Search Inactive').located_by("//*[contains(@class,'GameFilters__FilterButton') and text()='Inactive']")
    FIND_TITLE_SEARCH_EA = Target.the('Find Title Search EA').located_by("//*[contains(@class,'GameFilters__FilterButton') and text()='EA']")
    FIND_TITLE_SEARCH_NON_EA = Target.the('Find Title Search Non EA').located_by("//*[contains(@class,'GameFilters__FilterButton') and text()='Non-EA']")
    SECOND_COLLAPSED_TITLE_HEADER = Target.the('Second Collapsed Title Header').located_by("[class^='BaseGame'] [class^='CollapseHeader']")
    ALL_COLLAPSED_ITEM = Target.the('All Collapsed Item').located_by("//*[contains(@class,'CollapseItem')]/div[text()='All']")

    # Master Asset Table
    MASTER_ASSET_TABLE_FILTER_DROPDOWN = Target.the('Master Asset Filter On Master Asset Table').located_by("[class^='LightDropdown'] button")
    MASTER_ASSET_TABLE_HEADER = Target.the('Header Column On Master Asset Table').located_by("[class*='headerRow'] [class*='headerTruncatedText']")
    MASTER_ASSET_TABLE_BEAT = Target.the('Beat Column On Master Asset Table').located_by("[aria-colindex='1'] div span")
    MASTER_ASSET_TABLE_MASTER_NAME = Target.the('Name Of Master Name Column On Master Asset Table').located_by("[aria-colindex='2'] div span:nth-child(1)")
    MASTER_ASSET_TABLE_VOLTRON_ID = Target.the('Id Of Master Name Column On Master Asset Table').located_by("[aria-colindex='2'] div span:nth-child(2)")
    MASTER_ASSET_TABLE_YOUTUBE_VERSION = Target.the('YouTube Version Column On Master Asset Table').located_by("[class*='YoutubeVersionStatus'] >div:first-child")
    MASTER_ASSET_TABLE_YOUTUBE_METADATA = Target.the('YouTube Metadata Column On Master Asset Table').located_by("[class*='MetadataText']")
    MASTER_ASSET_TABLE_THUMBNAIL = Target.the('Thumbnail Column On Master Asset Table').located_by("[class*='ThumbnailWrapper']")
    MASTER_ASSET_TABLE_ASSET_TYPE = Target.the('Asset Type Column On Master Asset Table').located_by("[aria-colindex='6']")
    MASTER_ASSET_TABLE_GO_LIVE_DATE = Target.the('Go Live Date Column On Master Asset Table').located_by("[aria-colindex='7']")
    MASTER_ASSET_TABLE_ACTION = Target.the('Action Column On Master Asset Table').located_by("[class*='ActionContainer']")

    # YouTube Landing Dashboard
    YOUTUBE_LANDING_DASHBOARD_TABLE_HEADER = Target.the('Header Column On YouTube Landing Dashboard Table').located_by("[class*='headerRow'] [class*='headerTruncatedText']")
    YOUTUBE_LANDING_DASHBOARD_TABLE_VERSION_NAME = Target.the('Name Of Version Name Column On YouTube Landing Dashboard Table').located_by("[aria-colindex='1'] [class^='VersionAssetTable'] >div:first-child")
    YOUTUBE_LANDING_DASHBOARD_TABLE_LENGTH = Target.the('Length Of Version Name Column On YouTube Landing Dashboard Table').located_by("[aria-colindex='1'] [class^='VersionAssetTable'] >div:last-child")
    YOUTUBE_LANDING_DASHBOARD_TABLE_PUBLISH_STATUS = Target.the('Status Of Publish Status Column On YouTube Landing Dashboard Table').located_by("[aria-colindex='2'] [class*='StatusAndIcon'] div")
    YOUTUBE_LANDING_DASHBOARD_TABLE_EXTRACTED_LABEL = Target.the('Extracted Label Of Publish Status Column On YouTube Landing Dashboard Table').located_by("[aria-colindex='2'] [class*='ExtractedLabel']")
    YOUTUBE_LANDING_DASHBOARD_TABLE_METADATA_LOCALE = Target.the('Metadata Locale Column On YouTube Landing Dashboard Table').located_by("[aria-colindex='3'] [class*='LocaleColumn']")
    YOUTUBE_LANDING_DASHBOARD_TABLE_THUMBNAIL = Target.the('Thumbnail Column On YouTube Landing Dashboard Table').located_by("[aria-colindex='4'] [class*='Thumbnail']")
    YOUTUBE_LANDING_DASHBOARD_TABLE_PUBLISH_DATE = Target.the('Publish Date Column On YouTube Landing Dashboard Table').located_by("[aria-colindex='5']")
    YOUTUBE_LANDING_DASHBOARD_TABLE_CHANNEL = Target.the('Channel Column On YouTube Landing Dashboard Table').located_by("[aria-colindex='6']")
    YOUTUBE_LANDING_DASHBOARD_TABLE_YOUTUBE_LINK_WATCH = Target.the('Link To Watch Of YouTube Link Column On YouTube Landing Dashboard Table').located_by("[aria-colindex='7'] a:first-child")
    YOUTUBE_LANDING_DASHBOARD_TABLE_YOUTUBE_LINK_EDIT = Target.the('Link To Edit Of YouTube Link Column On YouTube Landing Dashboard Table').located_by("[aria-colindex='7'] a:last-child")
    YOUTUBE_LANDING_DASHBOARD_TABLE_EXTRACT_AND_IMPORT_YOUTUBE_METADATA_ICON = Target.the('Extract and Import YouTube Metadata Icon On YouTube Landing Dashboard Table').located_by("[aria-colindex='8'] svg")

    # Master Details
    TO_ASSET_UPLOAD_BUTTON = Target.the('To Asset Upload Button').located_by("//button[text()='TO ASSET UPLOAD']")
    TO_METADATA_EDIT_BUTTON = Target.the('To Metadata Edit Button').located_by("//button[text()='TO METADATA EDIT']")
    TO_PUBLISH_PAGE_BUTTON = Target.the('To Publish Page Button').located_by("//button[text()='TO PUBLISH PAGE']")
    EXTRACT_YOUTUBE_METADATA_BUTTON = Target.the('Extract Youtube Metadata Button').located_by("//button[text()='EXTRACT YOUTUBE METADATA']")
    COPY_YOUTUBE_LINKS_BUTTON = Target.the('Copy Youtube Links Button').located_by("//button[text()='COPY YOUTUBE LINKS']")

    # Extract YouTube Metadata Dialog
    EXTRACT_YOUTUBE_METADATA_DIALOG_YOUTUBE_ID_INPUT = Target.the('YouTube ID Input On Extract YouTube Metadata Dialog').located_by("[class^='ExtractorModal'] input")
    EXTRACT_YOUTUBE_METADATA_DIALOG_EXTRACT_METADATA_BUTTON = Target.the('Extract Metadata Button On Extract YouTube Metadata Dialog').located_by("//*[contains(@class,'BaseButton') and text()='EXTRACT METADATA']")
    EXTRACT_YOUTUBE_METADATA_DIALOG_CREATE_NEW_VERSION_BUTTON = Target.the('Create New Version Button On Extract YouTube Metadata Dialog').located_by("//*[contains(@class,'BaseButton') and text()='CREATE NEW VERSION']")
    EXTRACT_YOUTUBE_METADATA_DIALOG_IMPORT_YOUTUBE_METADATA_BUTTON = Target.the('Import YouTube Metadata Button On Extract YouTube Metadata Dialog').located_by("//*[contains(@class,'BaseButton') and text()='IMPORT YOUTUBE METADATA']")
    EXTRACT_YOUTUBE_METADATA_DIALOG_TABLE_HEADER = Target.the('Header Row On Extract YouTube Metadata Dialog').located_by("[class*='MetadataSection__HeaderRow'] [class*='HeaderCell']")
    EXTRACT_YOUTUBE_METADATA_DIALOG_VIDEO_TITLE = Target.the('Video Title On Extract YouTube Metadata Dialog').located_by("[class*='MetadataSection__MetadataRow'] >div:first-child")
    EXTRACT_YOUTUBE_METADATA_DIALOG_DESCRIPTION = Target.the('Description On Extract YouTube Metadata Dialog').located_by("[class*='MetadataSection__MetadataRow'] >div:nth-child(2)")
    EXTRACT_YOUTUBE_METADATA_DIALOG_SEARCH_TAGS = Target.the('Search Tags On Extract YouTube Metadata Dialog').located_by("[class*='MetadataSection__TagLabel']")
    EXTRACT_YOUTUBE_METADATA_DIALOG_THUMBNAIL = Target.the('Thumbnail On Extract YouTube Metadata Dialog').located_by("[class*='MetaCell'] img")
    EXTRACT_YOUTUBE_METADATA_DIALOG_YOUTUBE_PUBLISH = Target.the('YouTube Publish On Extract YouTube Metadata Dialog').located_by("[class*='MetaCell']:nth-child(5)")
    EXTRACT_YOUTUBE_METADATA_DIALOG_CHANNEL = Target.the('Channel On Extract YouTube Metadata Dialog').located_by("[class*='MetaCell']:nth-child(6)")

    # Create New Version Asset / Import YouTube Metadata Dialog
    CREATE_NEW_VERSION_ASSET_DIALOG_VERSION_NAME_INPUT = Target.the('Version Name Input On Create New Version Asset Dialog').located_by("input[class*='VersionNameInput']")
    CREATE_NEW_VERSION_ASSET_DIALOG_LOCALE_DROPDOWN = Target.the('Locale Dropdown On Create New Version Asset Dialog').located_by("[class*='CreateNewAssetModal__Wrapper'] [class*='CreateNewAssetModal__Section']:nth-child(2) button")
    CREATE_NEW_VERSION_ASSET_DIALOG_ASPECT_RATIO_DROPDOWN = Target.the('Aspect Ratio Dropdown On Create New Version Asset Dialog').located_by("[class*='CreateNewAssetModal__Wrapper'] [class*='CreateNewAssetModal__Section']:nth-child(3) button")
    CREATE_NEW_VERSION_ASSET_DIALOG_CHANNEL_DROPDOWN = Target.the('Channel Dropdown On Create New Version Asset Dialog').located_by("[class*='CreateNewAssetModal__Wrapper'] [class*='CreateNewAssetModal__Section']:nth-child(4) button")
    CREATE_NEW_VERSION_ASSET_DIALOG_DROPDOWN_SEARCH_INPUT = Target.the('Search Input In Dropdown List On Create New Version Asset Dialog').located_by("(//input[@placeholder='Search'])[last()]")
    CREATE_NEW_VERSION_ASSET_DIALOG_CREATE_NEW_VERSION_BUTTON = Target.the('Create New Version Button On Create New Version Asset Dialog').located_by("//*[contains(@class,'BaseButton') and text()='CREATE NEW VERSION']")
    CREATE_NEW_VERSION_ASSET_DIALOG_IMPORT_YOUTUBE_METADATA_BUTTON = Target.the('Import YoutTube Metadata Button On Create New Version Asset Dialog').located_by("//*[contains(@class,'BaseButton') and text()='IMPORT YOUTUBE METADATA']")

    def __init__(self, url):
        super().__init__(url)

    @staticmethod
    def get_master_asset_filter_option(filter_type: str) -> Target:
        return Target.the(f'{filter_type} Option In Master Asset Filter On Master Asset Table').located_by(
            f"//li[text()='{filter_type}']"
        )

    @staticmethod
    def get_master_asset_table_header(column: str) -> Target:
        return Target.the(f"Column Header '{column}' On Master Asset Table").located_by(f"[aria-label='{column}']")

    @staticmethod
    def get_master_asset_table_row(index: int) -> Target:
        return Target.the('Row On Master Asset Table').located_by(f"[aria-rowindex='{index + 1}']")

    @staticmethod
    def get_value_in_dropdown_list(keyword: str) -> Target:
        return Target.the(f'"{keyword}" Value In Dropdown List On Create New Version Asset Dialog').located_by(f"//li[contains(text(), '{keyword}')]")

    @staticmethod
    def get_youtube_landing_dashboard_table_version_name(version_name: str) -> Target:
        return Target.the(f'Version Name "{version_name}" On YouTube Landing Dashboard Table').located_by(f"[data-tip='{version_name}']")

    @staticmethod
    def get_youtube_link_by_version_name(version_name: str) -> Target:
        return Target.the(
            f'YouTube Link Of Version Name "{version_name}" On YouTube Landing Dashboard Table'
        ).located_by(
            f"(//div[@data-tip='{version_name}']/ancestor::div[3]/*/div[contains(@class, 'YoutubeIcons')]"
            f"/*/*[name()='svg'])[1]"
        )

    @staticmethod
    def get_youtube_studio_link_by_version_name(version_name: str) -> Target:
        return Target.the(
            f'YouTube Studio Link Of Version Name "{version_name}" On YouTube Landing Dashboard Table'
        ).located_by(
            f"(//div[@data-tip='{version_name}']/ancestor::div[3]/*/div[contains(@class, 'YoutubeIcons')]"
            f"/*/*[name()='svg'])[2]"
        )

    @staticmethod
    def get_import_youtube_metadata_icon_by_version_name(version_name: str) -> Target:
        return Target.the(
            f'YouTube Metadata Icon Of Version Name "{version_name}" On YouTube Landing Dashboard Table'
        ).located_by(
            f"//div[@data-tip='{version_name}']/ancestor::div[3]/*/div[contains(@class, 'YoutubeIcons')]/*[name()='svg']"
        )
