from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.abilities import BrowseTheWeb
from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from screenpy_selenium import Target

from questions.base_questions import BaseQuestions
from ui.youtube_hub import YoutubeHubPage


class YouTubeLandingDashboardData(BaseQuestions):

    def __init__(
            self,
            retrieve_row_by_version_name: str = None
    ) -> None:
        self.retrieve_row_by_version_name = retrieve_row_by_version_name
        self.headers = []

    @staticmethod
    def is_item_on_row_available(row: WebElement, item: Target):
        try:
            extracted_label = row.find_element(*item.locator)
            if extracted_label.is_displayed():
                return True
        except NoSuchElementException:
            return False

    def get_publish_status(self, row: WebElement) -> str:
        status = row.find_element(*YoutubeHubPage.YOUTUBE_LANDING_DASHBOARD_TABLE_PUBLISH_STATUS.locator).text
        extracted_label = YoutubeHubPage.YOUTUBE_LANDING_DASHBOARD_TABLE_EXTRACTED_LABEL
        if self.is_item_on_row_available(row, extracted_label):
            status += f", {row.find_element(*extracted_label.locator).text}"
        return status

    def get_metadata_locale(self, row: WebElement) -> str:
        metadata_locale = YoutubeHubPage.YOUTUBE_LANDING_DASHBOARD_TABLE_METADATA_LOCALE
        if self.is_item_on_row_available(row, metadata_locale):
            return row.find_element(*metadata_locale.locator).text
        return ""

    def get_youtube_links(self, row: WebElement) -> str:
        youtube_link_watch = YoutubeHubPage.YOUTUBE_LANDING_DASHBOARD_TABLE_YOUTUBE_LINK_WATCH
        youtube_link_edit = YoutubeHubPage.YOUTUBE_LANDING_DASHBOARD_TABLE_YOUTUBE_LINK_EDIT
        if self.is_item_on_row_available(row, youtube_link_watch):
            return f"{row.find_element(*youtube_link_watch.locator).get_attribute('href')}, " \
                   f"{row.find_element(*youtube_link_edit.locator).get_attribute('href')}"
        return ""

    def get_row_data(self, row: WebElement) -> dict:
        row_data = [
            f"{row.find_element(*YoutubeHubPage.YOUTUBE_LANDING_DASHBOARD_TABLE_VERSION_NAME.locator).text}, "
            f"{row.find_element(*YoutubeHubPage.YOUTUBE_LANDING_DASHBOARD_TABLE_LENGTH.locator).text}",
            self.get_publish_status(row),
            self.get_metadata_locale(row),
            row.find_element(*YoutubeHubPage.YOUTUBE_LANDING_DASHBOARD_TABLE_THUMBNAIL.locator).text,
            row.find_element(*YoutubeHubPage.YOUTUBE_LANDING_DASHBOARD_TABLE_PUBLISH_DATE.locator).text,
            row.find_element(*YoutubeHubPage.YOUTUBE_LANDING_DASHBOARD_TABLE_CHANNEL.locator).text,
            self.get_youtube_links(row),
        ]
        return dict(zip(self.headers, row_data))

    @beat('{} examines the data on YouTube Landing Dashboard Table')
    def answered_by(self, the_actor: Actor):
        data = []
        self.headers = self.get_texts(the_actor, YoutubeHubPage.YOUTUBE_LANDING_DASHBOARD_TABLE_HEADER)
        self.headers.pop()
        if self.retrieve_row_by_version_name:
            driver = the_actor.ability_to(BrowseTheWeb).browser
            driver.execute_script(
                'arguments[0].scrollIntoView()',
                YoutubeHubPage.get_youtube_landing_dashboard_table_version_name(self.retrieve_row_by_version_name).found_by(the_actor)
            )
        for row in YoutubeHubPage.ROW_TABLE.all_found_by(the_actor):
            row_data = self.get_row_data(row)
            data.append(row_data)
        if self.retrieve_row_by_version_name:
            return list(filter(lambda record: record['Version Name'].startswith(self.retrieve_row_by_version_name) is True, data))[0]
        return data
