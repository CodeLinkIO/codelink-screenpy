from screenpy_selenium import Target

from ui.base.base_page import BasePage
from ui.mixins import HeaderBarMixin


class AssetListGamePage(BasePage, HeaderBarMixin):

    TOAST_MESSAGE = Target.the('Toast Message').located_by("p[class^='Message__Text']")

    # Favourite Franchises Section
    FAVOURITE_FRANCHISE_NAME = Target.the('Franchise Name On Favourite Franchises Section').located_by("[data-cy=favouriteArea] [class^=Franchise__NameAndInfo] div:first-child")
    FAVOURITE_TITLE_NAME = Target.the('Title Name On Favourite Franchises Section').located_by("[data-cy=favouriteArea] [class^=SectionWrapper]:nth-child(4) [class^=Title__ThumbnailAndName]")

    # Search Section
    SEARCH_INPUT = Target.the('Search Input').located_by("input[class^='SearchMenu__Input']")
    SEARCH_ICON = Target.the('Search Icon').located_by("[class^='SearchMenu__Wrapper'] svg")
    RESULTS_MESSAGE = Target.the('Results Message').located_by("[class^='ResultArea__ErrorMessage']")

    # Data List
    FRANCHISE_NAME = Target.the('Franchise Name').located_by("[data-cy=resultArea] [class^=Franchise__NameAndInfo] div:first-child")
    TITLE_NAME = Target.the('Title Name').located_by("[class^=Title__ThumbnailAndName] [class^=TextHighlight]")
    BEAT_NAME = Target.the('Beat Name').located_by("[class^='BeatList__BeatInfo'] [class^='BeatList__NameAndDesc'] div:nth-of-type(1)")

    # Franchises List
    FRANCHISE_ACTIVE_TITLE_NUM = Target.the('Number Of Active Titles Of Franchise').located_by("[class^='Franchise__Header'] [class^='Franchise__NameAndInfo'] div:last-child")
    VIEW_FRANCHISE_TRACKER_LINK = Target.the('View Franchise Tracker Link').located_by("[href^='/assets/franchise/']")
    FAVOURITE_FRANCHISE_ICON = Target.the('Favourite Franchise Icon').located_by("[class^='Franchise__Header'] li:last-child svg")

    # Titles List
    VIEW_TITLE_TRACKER_LINK = Target.the('View Title Tracker Link').located_by("[href^='/assets/title/']")

    # Beats List
    BEAT_NAME_LINK = Target.the('Beat Name Link').located_by("[class^='BeatList__Row'] li:nth-child(1) [href^='/assets/title/'] ")
    SET_DEFAULT_LOCALES_BUTTON = Target.the('Set Default Locales Button').located_by("[title='Set default YouTube locales']")
    ADD_BEAT_BUTTON = Target.the('Add Beat Button').located_by("button[class*='add-beat-button']")
    EDIT_BEAT_BUTTON = Target.the('Edit Beat Button').located_by("[class^=BeatList__Row] li:last-child svg")
    VIEW_BEAT_LINK = Target.the('View Beat Link').located_by("[class^='BeatList__Row'] li:nth-child(4) [href^='/assets/title/'] ")
    SHOW_EMPTY_BEATS_CHECKBOX = Target.the('Show Empty Beats Checkbox').located_by("[class^='BeatHeader__LeftHeaderWrapper'] svg:first-child")
    BEATS_SORT_BY_DROPDOWN = Target.the('Beats Sort By Dropdown').located_by("[class^='BeatHeader__SortBy']")

    # Master Filter Section
    MASTER_FILTER = Target.the('Master Filter').located_by("[class^='MasterFilter__Header']")
    MASTER_FILTER_ACTIVE_TITLES_TOGGLE = Target.the('Filter Show Only Active Titles').located_by("#MasterFilter-ActiveTitleToggle")
    MASTER_FILTER_EA_TITLES_TOGGLE = Target.the('Filter Show Only EA Titles').located_by("[class^='MasterFilter__Body'] div:nth-of-type(2) span")
    MASTER_FILTER_ADDITIONAL_CONTENT_TOGGLE = Target.the('Filter Show Additional Content').located_by("[class^='MasterFilter__Body'] div:nth-of-type(3) span")

    # Add Beat Modal
    BEAT_MODAL_HEADER = Target.the('Beat Modal Header').located_by("[class^='Modal__Heading']")
    BEAT_MODAL_NAME_INPUT = Target.the('Beat Name Input').located_by("#name")
    BEAT_MODAL_PHASE_DROPDOWN = Target.the('Beat Phase Dropdown').located_by("[role='combobox']")
    BEAT_MODAL_START_DATE_INPUT = Target.the('Beat Start Date Datepicker').located_by("#start-date")
    BEAT_MODAL_END_DATE_INPUT = Target.the('Beat End Date Datepicker').located_by("#end-date")
    BEAT_MODAL_IS_EVERGREEN_CHECKBOX = Target.the('Beat Is Evergreen Checkbox').located_by("#is-evergreen")
    BEAT_MODAL_IS_EVERGREEN_FILL = Target.the('Beat Is Evergreen Fill').located_by("[class^=Checkbox__Label] path")
    BEAT_MODAL_CANCEL_BUTTON = Target.the('Cancel Button On Beat Modal').located_by("[class^='CancelButton']")
    BEAT_MODAL_CREATE_BUTTON = Target.the('Create Button On Beat Modal').located_by("[class^='Modal__Buttons'] button:nth-child(2)")
    BEAT_MODAL_SAVE_BUTTON = Target.the('Save Button On Beat Modal').located_by("[class^='Modal__Buttons'] button:nth-child(2)")
    BEAT_MODAL_CREATE_AND_ENTER_BUTTON = Target.the('Create And Enter Button On Beat Modal').located_by("[class^='Modal__Buttons'] button:last-child")
    BEAT_MODAL_SAVE_AND_ENTER_BUTTON = Target.the('Save And Enter Button On Beat Modal').located_by("[class^='Modal__Buttons'] button:last-child")
    BEAT_MODAL_CLOSE_BUTTON = Target.the('Close Button On Beat Modal').located_by("[class^='CloseButton']")

    # Set Default Locales Modal
    SET_DEFAULT_LOCALES_MODAL_SEARCH_INPUT = Target.the('Search Input On Set Default Youtube Locales Modal').located_by("[class=select-popup-content] input[type=search]")
    SET_DEFAULT_LOCALES_MODAL_CLOSE_BUTTON = Target.the('Close Button On Set Default Youtube Locales Modal').located_by("[role=tooltip] svg:first-child")
    SET_DEFAULT_LOCALES_MODAL_LOCALE_CHECKBOX = Target.the('Locale Checkbox On Set Default Youtube Locales Modal').located_by("[class^=Checkbox__Label]")

    def __init__(self, url):
        super().__init__(url)

    @staticmethod
    def get_num_filters_enabled_label(num_filters: int) -> Target:
        text = f"{num_filters} {'filter' if num_filters == 1 else 'filters'} enabled"
        return Target.the('Number Of Filers Enabled Label').located_by(
            f"//*[@id='MasterFilter']/div[contains(.,'{text}')]")

    @staticmethod
    def get_franchise_favourite_icon(franchise: str) -> Target:
        return Target.the('Franchise Favourite Icon').located_by(
            f"(//*[contains(@class,'Franchise__NameAndInfo')]//*[text()='{franchise}']/ancestor::ul//*[name()='svg'])[2]")

    @staticmethod
    def get_title_favourite_icon(title: str) -> Target:
        return Target.the('Title Favourite Icon').located_by(
            f"//*[contains(@class,'Title__ThumbnailAndName')]//*[text()='{title}']/ancestor::ul//*[name()='svg']")

    @staticmethod
    def get_title_link(title: str) -> Target:
        return Target.the('Title Link').located_by(
            f"//*[contains(@class,'TextHighlight') and text()='{title}']")
