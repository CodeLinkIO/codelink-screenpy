from enum import Enum

from screenpy import Actor
from screenpy.pacing import beat

from actions import WaitClick
from ui import YoutubeHubPage


class FilterMasterAssetType(Enum):
    SHOW_ALL_MASTER = 'Show all Master'
    SHOW_ONLY_MASTERS_WITH_NO_VERSION = 'Show only Masters with no versions'
    SHOW_ONLY_MASTERS_WITH_VERSION = 'Show only Masters with versions'


class FilterMasterAsset:

    def __init__(
            self,
            filter_type: FilterMasterAssetType = FilterMasterAssetType.SHOW_ALL_MASTER
    ):
        self.filter_type = filter_type
        self.filter_type_value = filter_type.value

    @beat("{} filters Master Asset Table with option '{filter_type_value}'.")
    def perform_as(self, the_actor: Actor) -> None:
        the_actor.attempts_to(
            WaitClick(YoutubeHubPage.MASTER_ASSET_TABLE_FILTER_DROPDOWN),
            WaitClick(YoutubeHubPage.get_master_asset_filter_option(self.filter_type_value))
        )
