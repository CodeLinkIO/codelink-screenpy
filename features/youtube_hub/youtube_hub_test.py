import os
import uuid
from datetime import datetime

from screenpy_selenium.actions import Click, Open
from screenpy_selenium.questions import TheText

from actions import WaitClick
from enums import MasterAssetTableAttribute
from features.base_test import BaseTest
from libraries.api_client.routes import Routes
from questions import ApiResponse, ClipboardText, NewTabUrl, ToastMessage
from questions.elastic_search import (GetMasterAssetsWithoutYouTubeVersion,
                                      GetMasterAssetsWithYouTubeVersion)
from questions.helpers.string_helpers import ReplaceStringUsingRegexp
from questions.youtube_hub import (MasterAssetTableData, ThumbnailStatusData,
                                   YouTubeLandingDashboardData,
                                   YouTubeMetadataData)
from questions.youtube_hub.youtube_version_published_disabled import PublishedYoutubeVersionDisabled
from screenpy import AnActor, given, then, when
from screenpy.actions import MakeNote, See
from screenpy.directions import noted_under
from screenpy.resolutions import (ContainTheEntry, ContainTheText, IsEqual,
                                  ReadsExactly)
from tasks import Login
from tasks.switch_to_new_tab import SwitchToNewTab
from tasks.youtube_hub import (AttachMasterThumbnail, AttachVersionThumbnail,
                               CreateNewVersionAsset, EditMetadata,
                               ExtractYouTubeMetadata, FilterMasterAsset,
                               FilterMasterAssetType, ImportYouTubeMetadata,
                               SearchGameTitle, SearchMasterAsset,
                               SortMasterAsset, SortMasterAssetColumn)
from tasks.youtube_hub.publish_youtube_version import PublishYoutubeVersion
from ui import YoutubeHubPage
from ui.metadata_edit import MetadataEditPage


class TestYoutubeHub(BaseTest):

    def test_youtube_hub_master_asset_view(self, the_qa_engineer_2: AnActor):
        given(the_qa_engineer_2).was_able_to(
            Open.their_browser_on(self.pages['YOUTUBE_HUB_PAGE'].url)
        )
        when(the_qa_engineer_2).attempts_to(
            MakeNote.of_the("chivu").as_("username"),
            MakeNote.of_the("123456").as_("password")
        )
        # Show all Master on Master Asset table
        when(the_qa_engineer_2).attempts_to(
            Login(noted_under("username"), noted_under("password")),
            SearchGameTitle(keyword="Voltron"),
            MakeNote.of_the(ApiResponse(Routes.TITLES, timeout=20)).as_("titles"),
            FilterMasterAsset(FilterMasterAssetType.SHOW_ALL_MASTER)
        )
        when(the_qa_engineer_2).attempts_to(
            MakeNote.of_the(noted_under("titles")["game"]["id"]).as_("game_id")
        )
        when(the_qa_engineer_2).attempts_to(
            MakeNote.of_the(GetMasterAssetsWithYouTubeVersion(
                path=self.pages['CORE_URL'],
                game_id=noted_under("game_id"),
                username=noted_under("username"),
                password=noted_under("password")
            )).as_("master_assets_with_youtube_version"),
            MakeNote.of_the(GetMasterAssetsWithoutYouTubeVersion(
                path=self.pages['CORE_URL'],
                game_id=noted_under("game_id"),
                username=noted_under("username"),
                password=noted_under("password")
            )).as_("master_assets_without_youtube_version")
        )
        when(the_qa_engineer_2).attempts_to(
            MakeNote.of_the(
                noted_under("master_assets_with_youtube_version") + [
                    {MasterAssetTableAttribute.MASTER_NAME: d[MasterAssetTableAttribute.MASTER_NAME],
                     MasterAssetTableAttribute.VOLTRON_ID: d[MasterAssetTableAttribute.VOLTRON_ID]}
                    for d in noted_under("master_assets_without_youtube_version")
                ]
            ).as_("all_master_assets"),
            MakeNote.of_the(MasterAssetTableData()).as_("actual_master_assets_data")
        )
        then(the_qa_engineer_2).should(
            See.the(sorted(noted_under("actual_master_assets_data"),
                           key=lambda d: d[MasterAssetTableAttribute.VOLTRON_ID]),
                    IsEqual(sorted(noted_under("all_master_assets"),
                            key=lambda d: d[MasterAssetTableAttribute.VOLTRON_ID])))
        )
        # Show only Masters with versions on Master Asset table
        when(the_qa_engineer_2).attempts_to(
            Open.their_browser_on(self.pages['YOUTUBE_HUB_PAGE'].url),
            SearchGameTitle(keyword="Voltron"),
            FilterMasterAsset(FilterMasterAssetType.SHOW_ONLY_MASTERS_WITH_VERSION),
            MakeNote.of_the(MasterAssetTableData()).as_("actual_master_assets_data")
        )
        then(the_qa_engineer_2).should(
            See.the(sorted(noted_under("actual_master_assets_data"),
                           key=lambda d: d[MasterAssetTableAttribute.VOLTRON_ID]),
                    IsEqual(sorted(noted_under("master_assets_with_youtube_version"),
                            key=lambda d: d[MasterAssetTableAttribute.VOLTRON_ID])))
        )
        # Show only Masters with no versions on Master Asset table
        when(the_qa_engineer_2).attempts_to(
            FilterMasterAsset(FilterMasterAssetType.SHOW_ONLY_MASTERS_WITH_NO_VERSION),
            MakeNote.of_the(MasterAssetTableData(
                data=[MasterAssetTableAttribute.MASTER_NAME,
                      MasterAssetTableAttribute.VOLTRON_ID,
                      MasterAssetTableAttribute.BEAT,
                      MasterAssetTableAttribute.GO_LIVE_DATE]
            )).as_("actual_master_assets_data")
        )
        then(the_qa_engineer_2).should(
            See.the(sorted(noted_under("actual_master_assets_data"),
                           key=lambda d: d[MasterAssetTableAttribute.VOLTRON_ID]),
                    IsEqual(sorted(noted_under("master_assets_without_youtube_version"),
                            key=lambda d: d[MasterAssetTableAttribute.VOLTRON_ID])))
        )
        # Sort Master Asset table by Beat
        when(the_qa_engineer_2).attempts_to(
            SortMasterAsset(SortMasterAssetColumn.BEAT),
            MakeNote.of_the(MasterAssetTableData(
                data=[MasterAssetTableAttribute.MASTER_NAME,
                      MasterAssetTableAttribute.VOLTRON_ID,
                      MasterAssetTableAttribute.BEAT,
                      MasterAssetTableAttribute.GO_LIVE_DATE]
            )).as_("actual_master_assets_data")
        )
        then(the_qa_engineer_2).should(See.the(
            noted_under("actual_master_assets_data"),
            IsEqual(sorted(
                sorted(
                    sorted(noted_under("master_assets_without_youtube_version"),
                           key=lambda d: d[MasterAssetTableAttribute.MASTER_NAME]),
                    key=lambda d: datetime.strptime(d[MasterAssetTableAttribute.GO_LIVE_DATE], "%b %d, %Y") if d[MasterAssetTableAttribute.GO_LIVE_DATE] != "-" else datetime.now(),
                    reverse=True
                ),
                key=lambda d: d[MasterAssetTableAttribute.BEAT]
            )))
        )
        # Sort Master Asset table by Master Name
        when(the_qa_engineer_2).attempts_to(
            SortMasterAsset(SortMasterAssetColumn.MASTER_NAME),
            MakeNote.of_the(MasterAssetTableData(
                data=[MasterAssetTableAttribute.MASTER_NAME,
                      MasterAssetTableAttribute.VOLTRON_ID,
                      MasterAssetTableAttribute.BEAT,
                      MasterAssetTableAttribute.GO_LIVE_DATE]
            )).as_("actual_master_assets_data")
        )
        then(the_qa_engineer_2).should(
            See.the(
                noted_under("actual_master_assets_data"),
                IsEqual(sorted(noted_under("master_assets_without_youtube_version"),
                               key=lambda d: d[MasterAssetTableAttribute.MASTER_NAME]))
            )
        )
        # Sort Master Asset table by Go Live Date
        when(the_qa_engineer_2).attempts_to(
            SortMasterAsset(SortMasterAssetColumn.GO_LIVE_DATE),
            MakeNote.of_the(MasterAssetTableData(
                data=[MasterAssetTableAttribute.MASTER_NAME,
                      MasterAssetTableAttribute.VOLTRON_ID,
                      MasterAssetTableAttribute.BEAT,
                      MasterAssetTableAttribute.GO_LIVE_DATE]
            )).as_("actual_master_assets_data")
        )
        then(the_qa_engineer_2).should(
            See.the(
                noted_under("actual_master_assets_data"),
                IsEqual(
                    sorted(
                        sorted(noted_under("master_assets_without_youtube_version"),
                               key=lambda d: d[MasterAssetTableAttribute.MASTER_NAME], reverse=True),
                        key=lambda d: datetime.strptime(d[MasterAssetTableAttribute.GO_LIVE_DATE], "%b %d, %Y") if d[MasterAssetTableAttribute.GO_LIVE_DATE] != "-" else datetime.now()
                    )
                )
            )
        )
        # Search Master Asset ID and To Metadata Edit
        when(the_qa_engineer_2).attempts_to(
            SearchMasterAsset(keyword="00djk"),
            MakeNote.of_the(ApiResponse(Routes.ASSETS)).as_("assets_by_ids_response"),
            WaitClick(YoutubeHubPage.TO_METADATA_EDIT_BUTTON)
        )
        when(the_qa_engineer_2).attempts_to(
            MakeNote.of_the(noted_under("assets_by_ids_response")["id"]).as_("assets_id"),
        )
        then(the_qa_engineer_2).should(
            See.the(
                NewTabUrl(),
                IsEqual(f"{self.pages['YOUTUBE_HUB_PAGE'].url}youtube-configurator/{noted_under('assets_id')}")
            )
        )
        # To Publish Page
        when(the_qa_engineer_2).attempts_to(
            WaitClick(YoutubeHubPage.TO_PUBLISH_PAGE_BUTTON)
        )
        then(the_qa_engineer_2).should(
            See.the(
                NewTabUrl(),
                IsEqual(f"{self.pages['YOUTUBE_HUB_PAGE'].url}youtube-publish/{noted_under('assets_id')}")
            )
        )

    def test_youtube_hub_create_new_version(self, the_qa_engineer_2: AnActor):
        given(the_qa_engineer_2).was_able_to(
            Open.their_browser_on(self.pages['YOUTUBE_HUB_PAGE'].url)
        )
        when(the_qa_engineer_2).attempts_to(
            MakeNote.of_the("chivu").as_("username"),
            MakeNote.of_the("123456").as_("password"),
            MakeNote.of_the("UBeL2GXOb_Y").as_("youtube_id"),
            MakeNote.of_the("Ireland - English").as_("locale"),
            MakeNote.of_the("00c98").as_("master_asset_id")
        )
        when(the_qa_engineer_2).attempts_to(
        )
        # Extract Youtube Metadata
        when(the_qa_engineer_2).attempts_to(
            Login(noted_under("username"), noted_under("password")),
            SearchMasterAsset(noted_under("master_asset_id")),
            WaitClick(YoutubeHubPage.EXTRACT_YOUTUBE_METADATA_BUTTON),
            ExtractYouTubeMetadata(noted_under("youtube_id")),
            MakeNote.of_the(
                ApiResponse(Routes.YOUTUBE_METADATA_EXTRACTOR, timeout=20)
            ).as_("youtube_metadata_response"),
        )
        when(the_qa_engineer_2).attempts_to(
            MakeNote.of_the(
                ReplaceStringUsingRegexp(
                    noted_under("youtube_metadata_response")["description"],
                    "\n|\n\n|\xa0"
                )
            ).as_("description"),
        )
        when(the_qa_engineer_2).attempts_to(
            MakeNote.of_the({
                'Video Title': noted_under("youtube_metadata_response")["title"],
                'Description': noted_under("description"),
                'Search Tags': [tag.replace("\xa0", "") for tag in noted_under("youtube_metadata_response")["tags"]],
                'Thumbnail': noted_under("youtube_metadata_response")["thumbnails"]["default"]["url"],
                "YouTube Publish": datetime.strptime(
                    noted_under("youtube_metadata_response")["published_at"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S"
                ).strftime("%b %d, %Y"),
                'Channel': noted_under("youtube_metadata_response")["channel_title"]
            }).as_("expected_youtube_metadata")
        )
        then(the_qa_engineer_2).should(
            See.the(
                YouTubeMetadataData(),
                ContainTheEntry(**noted_under("expected_youtube_metadata"))
            )
        )
        # Create New Version Asset
        when(the_qa_engineer_2).attempts_to(
            MakeNote.of_the(f"Auto_Version_Name_{str(uuid.uuid4())}").as_("version_name"),
            MakeNote.of_the("Ireland - English").as_("locale"),
            MakeNote.of_the("9:4").as_("aspect_ratio"),
            MakeNote.of_the("YouTube owned").as_("channel"),
            MakeNote.of_the(
                f"https://www.youtube.com/watch?v={noted_under('youtube_id')}"
            ).as_("youtube_link"),
            MakeNote.of_the(
                f"https://studio.youtube.com/video/{noted_under('youtube_id')}/edit"
            ).as_("youtube_studio_link")
        )
        when(the_qa_engineer_2).attempts_to(
            MakeNote.of_the({
                "Version Name": f"{noted_under('version_name')}, Length: Longform",
                "Publish Status": "Successful, EXTRACTED",
                "Metadata Locale": "EN - IE",
                "Thumbnail": "ASSIGNED",
                "Channel": noted_under("youtube_metadata_response")["channel_title"],
                "Publish Date": datetime.strptime(
                    noted_under("youtube_metadata_response")["published_at"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S"
                ).strftime("%b %d, %Y"),
                "YouTube Link": f"{noted_under('youtube_link')}, {noted_under('youtube_studio_link')}"
            }).as_("expected_youtube_landing_dashboard_row"),
        )
        when(the_qa_engineer_2).attempts_to(
            Click(YoutubeHubPage.EXTRACT_YOUTUBE_METADATA_DIALOG_CREATE_NEW_VERSION_BUTTON),
            CreateNewVersionAsset(
                version_name=noted_under('version_name'),
                locale=noted_under('locale'),
                aspect_ratio=noted_under('aspect_ratio'),
                channel=noted_under('channel')
            )
        )
        then(the_qa_engineer_2).should(
            See.the(
                YouTubeLandingDashboardData(retrieve_row_by_version_name=noted_under('version_name')),
                ContainTheEntry(**noted_under("expected_youtube_landing_dashboard_row"))
            ),
        )
        # Click YouTube link
        when(the_qa_engineer_2).attempts_to(
            Click(YoutubeHubPage.get_youtube_link_by_version_name(noted_under('version_name')))
        )
        then(the_qa_engineer_2).should(
            See.the(
                NewTabUrl(),
                IsEqual(noted_under('youtube_link'))
            )
        )
        # Click YouTube Studio link
        # It requires authentication to access YouTube Studio
        # when(the_qa_engineer_2).attempts_to(
        #     Click(YoutubeHubPage.get_youtube_studio_link_by_version_name(noted_under('version_name')))
        # )
        # then(the_qa_engineer_2).should(
        #     See.the(NewTabUrl(), IsEqual(noted_under('youtube_studio_link')))
        # )

    def test_youtube_hub_import_youtube_metadata(self, the_qa_engineer_2: AnActor):
        given(the_qa_engineer_2).was_able_to(
            Open.their_browser_on(self.pages['YOUTUBE_HUB_PAGE'].url)
        )
        when(the_qa_engineer_2).attempts_to(
            MakeNote.of_the("chivu").as_("username"),
            MakeNote.of_the("123456").as_("password")
        )
        when(the_qa_engineer_2).attempts_to(
            Login(noted_under("username"), noted_under("password")),
            MakeNote.of_the("Mqk7FuTQAyQ").as_("youtube_id"),
            MakeNote.of_the("00cmu").as_("master_asset_id")
        )
        when(the_qa_engineer_2).attempts_to(
            MakeNote.of_the("SWJFO_E3Demo29min_OWNED_YT_1080p_16x9_29-97fps_LF_SPA_XM").as_("version_name"),
            MakeNote.of_the("Ireland - English").as_("locale"),
            MakeNote.of_the("9:4").as_("aspect_ratio"),
            MakeNote.of_the("YouTube owned").as_("channel"),
            MakeNote.of_the(
                f"https://www.youtube.com/watch?v={noted_under('youtube_id')}"
            ).as_("youtube_link"),
            MakeNote.of_the(
                f"https://studio.youtube.com/video/{noted_under('youtube_id')}/edit"
            ).as_(
                "youtube_studio_link")
        )
        # Import YouTube Metadata
        when(the_qa_engineer_2).attempts_to(
            SearchMasterAsset(noted_under("master_asset_id")),
            WaitClick(YoutubeHubPage.get_import_youtube_metadata_icon_by_version_name(noted_under("version_name"))),
            ExtractYouTubeMetadata(noted_under("youtube_id")),
            MakeNote.of_the(ApiResponse(Routes.YOUTUBE_METADATA_EXTRACTOR, timeout=20)).as_(
                "youtube_metadata_response"),
            Click(YoutubeHubPage.EXTRACT_YOUTUBE_METADATA_DIALOG_IMPORT_YOUTUBE_METADATA_BUTTON),
            ImportYouTubeMetadata(locale=noted_under('locale'))
        )
        when(the_qa_engineer_2).attempts_to(
            MakeNote.of_the({
                "Version Name": f"{noted_under('version_name')}, Length: Longform",
                "Publish Status": "Successful, EXTRACTED",
                "Metadata Locale": "EN - IE",
                "Thumbnail": "ASSIGNED",
                "Channel": noted_under("youtube_metadata_response")["channel_title"],
                "Publish Date": datetime.strptime(
                    noted_under("youtube_metadata_response")["published_at"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S"
                ).strftime("%b %d, %Y"),
                "YouTube Link": f"{noted_under('youtube_link')}, {noted_under('youtube_studio_link')}"
            }).as_("expected_youtube_landing_dashboard_row"),
        )
        then(the_qa_engineer_2).should(
            See.the(
                YouTubeLandingDashboardData(retrieve_row_by_version_name=noted_under('version_name')),
                ContainTheEntry(**noted_under("expected_youtube_landing_dashboard_row"))
            )
        )
        # Copy YouTube Links
        when(the_qa_engineer_2).attempts_to(WaitClick(YoutubeHubPage.COPY_YOUTUBE_LINKS_BUTTON))
        then(the_qa_engineer_2).should(
            See.the(ToastMessage(), ContainTheText("link(s) copied to clipboard")),
            See.the(ClipboardText(), ContainTheText(noted_under('locale').split("-")[0].strip())),
            See.the(ClipboardText(), ContainTheText(noted_under('locale').split("-")[1].strip())),
            See.the(ClipboardText(), ContainTheText(noted_under('version_name'))),
            See.the(ClipboardText(), ContainTheText(noted_under('youtube_link')))
        )

    def test_youtube_hub_publish_youtube_video(self, the_qa_engineer_2: AnActor):
        given(the_qa_engineer_2).was_able_to(
            Open.their_browser_on(self.pages['YOUTUBE_HUB_PAGE'].url)
        )
        when(the_qa_engineer_2).attempts_to(
            MakeNote.of_the("chivu").as_("username"),
            MakeNote.of_the("123456").as_("password"),
            MakeNote.of_the("fr-FR").as_("locale"),
            MakeNote.of_the(str(uuid.uuid4())).as_("title"),
            MakeNote.of_the(str(uuid.uuid4())).as_("description"),
            MakeNote.of_the(str(uuid.uuid4()).split("-")).as_("tags")
        )
        # Edit metadata
        when(the_qa_engineer_2).attempts_to(
            Login(noted_under("username"), noted_under("password")),
            SearchMasterAsset(keyword="00cjn"),
            WaitClick(YoutubeHubPage.TO_METADATA_EDIT_BUTTON),
            SwitchToNewTab(),
            EditMetadata(locale=noted_under("locale"),
                         title=noted_under("title"),
                         description=noted_under("description"),
                         tags=noted_under("tags")),
        )
        then(the_qa_engineer_2).should(
            See(
                TheText.of_the(MetadataEditPage.VALIDATE_BUTTON),
                ReadsExactly("Validated")
            )
        )
        # Attach master thumbnail image
        when(the_qa_engineer_2).attempts_to(
            AttachMasterThumbnail(f"{os. getcwd()}/resources/images/thumbnail.png"),
            MakeNote.of_the(ThumbnailStatusData()).as_("actual_thumbnail_status")
        )
        when(the_qa_engineer_2).attempts_to(
            MakeNote.of_the(
                ["MASTER THUMBNAIL"] * len(noted_under("actual_thumbnail_status"))
            ).as_("expected_thumbnail_status")
        )
        then(the_qa_engineer_2).should(
            See(noted_under("actual_thumbnail_status"), IsEqual(noted_under("expected_thumbnail_status")))
        )
        # Attach version thumbnail image
        when(the_qa_engineer_2).attempts_to(
            AttachVersionThumbnail(f"{os. getcwd()}/resources/images/thumbnail.png"),
            MakeNote.of_the(ThumbnailStatusData()).as_("actual_thumbnail_status"),
            MakeNote.of_the(
                ["VERSION THUMBNAIL" if i == 0 else 'MASTER THUMBNAIL' for i in
                 range(len(noted_under("actual_thumbnail_status")))]
            ).as_("expected_thumbnail_status")
        )
        then(the_qa_engineer_2).should(
            See(noted_under("actual_thumbnail_status"), IsEqual(noted_under("expected_thumbnail_status")))
        )
        # Publish YouTube version
        when(the_qa_engineer_2).attempts_to(
            Click.on_the(MetadataEditPage.ATTACH_THUMBNAILS_TAB),
            MakeNote.of_the("Apex_s02_IronCrown").as_("file_name")
        )
        when(the_qa_engineer_2).attempts_to(
            Click.on_the(MetadataEditPage.PUBLISH_BUTTON),
        )
        when(the_qa_engineer_2).attempts_to(
            PublishYoutubeVersion(
                file_name=noted_under("file_name"),
                metadata_locale=noted_under("locale"),
                youtube_channels="CTI Test Channel"
            )
        )
        then(the_qa_engineer_2).should(
            See(PublishedYoutubeVersionDisabled(noted_under("file_name")), IsEqual(True))
        )
