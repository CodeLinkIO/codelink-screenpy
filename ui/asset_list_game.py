from enum import Enum

from screenpy_selenium import Target

from ui.base.base_page import BasePage


class Franchise(Enum):
    PLAGUE_TALE_INNOCENCE = 'A Plague Tale Innocence'
    BATTLEFIELD = 'Battlefield'
    COMMAND_AND_CONQUER = 'Command & Conquer'
    DEAD_SPACE = 'Dead Space'
    DRAGON_AGE = 'Dragon Age'
    FIFA = 'FIFA'
    MADDEN = 'Madden'
    ROCKET_ARENA = 'Rocket Arena'
    STAR_WARS = 'Star Wars'
    VOLTRON = 'Voltron'


class AssetListGamePage(BasePage):

    FRANCHISE_FMT = '//div[contains(@class, \'Franchise__NameAndInfo\')]/div[text()=\'%s\']'
    VIEW_FRANCHISE_TRACKER_FMT = FRANCHISE_FMT + '/ancestor::li/following-sibling::li/*//button[text()=\'View Franchise Tracker\']'
    FAVORITE_FRANCHISE_FMT = FRANCHISE_FMT + '/ancestor::li/following-sibling::li/*[name()=\'svg\']'
    TITLE_FMT = '//ul[contains(@class, \'Title__Header\')]//strong[text()=\'%s\']'
    VIEW_TITLE_TRACKER_FMT = TITLE_FMT + '/ancestor::li/following-sibling::li/*//button[text()=\'View Title Tracker\']'
    FAVORITE_TITLE_FMT = TITLE_FMT + '/ancestor::li/following-sibling::li/*[name()=\'svg\']'
    BEAT_FMT = '//div[contains(@class, \'BeatList__NameAndDesc\')]/div[text()=\'%s\']'
    VIEW_BEAT_FMT = BEAT_FMT + '/ancestor::li/following-sibling::li[3]/a[text()=\'View Beat\']'
    BEAT_SETTING_FMT = BEAT_FMT + '/ancestor::li/following-sibling::li[4]/*[name()=\'svg\']'

    HEADER = Target.the('The Title').located_by('//h1[text()=\'Franchises, Titles & Beats\']')

    # Search Section
    SEARCH_INPUT = Target.the('The Search Input').located_by('//input[@placeholder=\'Search for Beat, Title or Franchise...\']')
    SEARCH_ICON = Target.the('The Search Icon').located_by('//div[contains(@class, \'SearchMenu__Wrapper\')]//*[name()=\'svg\']')
    NO_RESULTS_FOUND_ERROR_MESSAGE = Target.the('No Results Found Error Message').located_by('//div=[text()=\'No entries found. Please check your filters.\']')

    # Master Filter Section
    MASTER_FILTER = Target.the('The Master Filter').located_by('//div[contains(@class, \'MasterFilter__Header\')]')
    MASTER_FILTER_ACTIVE_TITLES_TOGGLE = Target.the('The Filter Show Only Active Titles').located_by('//div[text()=\'Show only active titles\']/span')
    MASTER_FILTER_EA_TITLES_TOGGLE = Target.the('The Filter Show Only Active Titles').located_by('//div[text()=\'Show only EA titles\']/span')
    MASTER_FILTER_ADDITIONAL_CONTENT_TOGGLE = Target.the('The Filter Show Additional Content').located_by('//div[text()=\'Show additional content\']/span')

    # Beats List Section
    SET_DEFAULT_LOCALES_BUTTON = Target.the('The Set Default Locales Button').located_by('//span[text()=\'+ Set default locales\']')
    ADD_BEAT_BUTTON = Target.the('The Add Beat Button').located_by('//button[text()=\'+ Add Beat\']')
    SHOW_EMPTY_BEATS_CHECKBOX = Target.the('The Show Empty Beats Checkbox').located_by('//div[contains(text(), \'Show empty beats\')]')
    BEATS_SORT_BY_DROPDOWN = Target.the('The Beats Sort By Dropdown').located_by('//div[contains(@class, \'BeatHeader__SortBy\')]')

    # Add Beat Modal
    BEAT_MODAL_ADD_BEAT_TITLE = Target.the('The Add Beat Title').located_by('//div[text()=\'Add Beat\']')
    BEAT_MODAL_EDIT_BEAT_TITLE = Target.the('The Edit Beat Title').located_by('//div[text()=\'Edit Beat\']')
    BEAT_MODAL_NAME_INPUT = Target.the('The Beat Name Input').located_by('//input[contains(@class, \'BeatModal__Input\')]')
    BEAT_MODAL_PHASE_DROPDOWN = Target.the('The Beat Phase Dropdown').located_by('//label[@for=\'phase\']/../div/div[@role=\'combobox\']')
    BEAT_MODAL_START_DATE_INPUT = Target.the('The Beat Start Date Datepicker').located_by('//input[@id=\'start-date\']')
    BEAT_MODAL_END_DATE_INPUT = Target.the('The Beat End Date Datepicker').located_by('//input[@id=\'end-date\']')
    BEAT_MODAL_IS_EVERGREEN_CHECKBOX = Target.the('The Beat Is Evergreen Checkbox').located_by('//input[@id=\'is-evergreen\']')
    BEAT_MODAL_CANCEL_BUTTON = Target.the('The Cancel Button On Beat Modal').located_by('//button[text()=\'Cancel\']')
    BEAT_MODAL_CREATE_BUTTON = Target.the('The Create Button On Beat Modal').located_by('//button[text()=\'Create\']')
    BEAT_MODAL_SAVE_BUTTON = Target.the('The Save Button On Beat Modal').located_by('//button[text()=\'Save\']')
    BEAT_MODAL_CREATE_AND_ENTER_BUTTON = Target.the('The Create And Enter Button On Beat Modal').located_by('//button[text()=\'Create & Enter\']')
    BEAT_MODAL_SAVE_AND_ENTER_BUTTON = Target.the('The Save And Enter Button On Beat Modal').located_by('//button[text()=\'Save & Enter\']')
    BEAT_MODAL_CLOSE_BUTTON = Target.the('The Close Button On Beat Modal').located_by('//div[contains(@class, \'Modal__Heading\')]/*[name()=\'svg\']')

    def __init__(self, url):
        super().__init__(url)

    def get_franchise(self, franchise: Franchise) -> Target:
        return Target.the('The Franchise').located_by(
            self.FRANCHISE_FMT % franchise.value
        )

    def get_view_franchise_tracker_link(self, franchise_menu: Franchise) -> Target:
        return Target.the('The View Franchise Tracker Link').located_by(
            self.VIEW_FRANCHISE_TRACKER_FMT % franchise_menu.value
        )

    def get_franchise_favorite_icon(self, franchise_menu: Franchise) -> Target:
        return Target.the('The Franchise Favorite Icon').located_by(
            self.FAVORITE_FRANCHISE_FMT % franchise_menu.value
        )

    def get_title(self, title: str) -> Target:
        return Target.the('The Title').located_by(
            self.TITLE_FMT % title
        )

    def get_view_title_tracker_link(self, title: str) -> Target:
        return Target.the('The View Title Tracker Link').located_by(
            self.VIEW_TITLE_TRACKER_FMT % title
        )

    def get_title_favorite_icon(self, title: str) -> Target:
        return Target.the('The Title Favorite Icon').located_by(
            self.FAVORITE_FRANCHISE_FMT % title
        )

    def get_view_beat_button(self, beat: str) -> Target:
        return Target.the('The View Beat Link').located_by(
            self.VIEW_BEAT_FMT % beat
        )

    def get_beat_setting_icon(self, beat: str) -> Target:
        return Target.the('The Beat Setting Icon').located_by(
            self.BEAT_SETTING_FMT % beat
        )
