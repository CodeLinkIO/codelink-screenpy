import typing
import logging

from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.abilities import BrowseTheWeb
from screenpy_selenium.exceptions import TargetingError
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from enums.master_asset_table_attribute import MasterAssetTableAttribute
from questions.base_questions import BaseQuestions
from ui.youtube_hub import YoutubeHubPage


class MasterAssetTableData(BaseQuestions):

    def __init__(
            self,
            data: typing.List[MasterAssetTableAttribute] = None,
            sorted_by: MasterAssetTableAttribute = None
    ) -> None:
        if data is None:
            data = [MasterAssetTableAttribute.MASTER_NAME, MasterAssetTableAttribute.VOLTRON_ID]
        self.data = data
        self.sorted_by = sorted_by

    MASTER_ASSET_TABLE_ROW_DATA_LOCATORS_MAPPING = {
        MasterAssetTableAttribute.BEAT: YoutubeHubPage.MASTER_ASSET_TABLE_BEAT,
        MasterAssetTableAttribute.MASTER_NAME: YoutubeHubPage.MASTER_ASSET_TABLE_MASTER_NAME,
        MasterAssetTableAttribute.VOLTRON_ID: YoutubeHubPage.MASTER_ASSET_TABLE_VOLTRON_ID,
        MasterAssetTableAttribute.YOUTUBE_VERSION: YoutubeHubPage.MASTER_ASSET_TABLE_YOUTUBE_VERSION,
        MasterAssetTableAttribute.YOUTUBE_METADATA: YoutubeHubPage.MASTER_ASSET_TABLE_YOUTUBE_METADATA,
        MasterAssetTableAttribute.THUMBNAIL: YoutubeHubPage.MASTER_ASSET_TABLE_THUMBNAIL,
        MasterAssetTableAttribute.ASSET_TYPE: YoutubeHubPage.MASTER_ASSET_TABLE_ASSET_TYPE,
        MasterAssetTableAttribute.GO_LIVE_DATE: YoutubeHubPage.MASTER_ASSET_TABLE_GO_LIVE_DATE
    }

    @staticmethod
    def get_action(the_actor: Actor):
        data = []
        for element in YoutubeHubPage.MASTER_ASSET_TABLE_ACTION.all_found_by(the_actor):
            actions_in_a_row = [el.text for el in element.find_elements(By.CSS_SELECTOR, "a")]
            data.append(actions_in_a_row)
        return data

    def get_voltron_id(self, row: WebElement, the_actor: Actor):
        text = row.find_element(
            *self.MASTER_ASSET_TABLE_ROW_DATA_LOCATORS_MAPPING.get(
                MasterAssetTableAttribute.VOLTRON_ID).locator
        ).text
        voltron_id = text.split(":")[1].strip()
        return voltron_id

    def get_headers(self, the_actor: Actor):
        headers = self.get_texts(the_actor, YoutubeHubPage.MASTER_ASSET_TABLE_HEADER)
        return headers

    def get_row_data(self, the_actor: Actor, row: WebElement) -> dict:
        row_data = []
        for item in self.data:
            if item == MasterAssetTableAttribute.ACTION:
                row_data.append(
                    self.get_action(the_actor)
                )
            elif item == MasterAssetTableAttribute.VOLTRON_ID:
                row_data.append(
                    self.get_voltron_id(row, the_actor)
                )
            else:
                row_data.append(
                    row.find_element(*self.MASTER_ASSET_TABLE_ROW_DATA_LOCATORS_MAPPING.get(item).locator).text
                )
        return dict(zip(self.data, row_data))

    @beat('{} examines the data on Master Asset Table')
    def answered_by(self, the_actor: Actor):
        data = []
        driver = the_actor.ability_to(BrowseTheWeb).browser
        bottom_reached = False
        i = 0
        while not bottom_reached:
            target = YoutubeHubPage.get_master_asset_table_row(i)
            try:
                target.found_by(the_actor)
            except TargetingError:
                driver.execute_script(
                    'arguments[0].scrollIntoView()',
                    YoutubeHubPage.get_master_asset_table_row(i - 1).found_by(the_actor)
                )
            try:
                row_data = self.get_row_data(the_actor, target.found_by(the_actor))
                data.append(row_data)
            except TargetingError:
                bottom_reached = True
            i += 1
        if self.sorted_by:
            return sorted(data, key=lambda d: d[self.sorted_by])
        return data
