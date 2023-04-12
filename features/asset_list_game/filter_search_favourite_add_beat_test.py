import uuid

from screenpy import AnActor, given, when, then
from screenpy.actions import See
from screenpy.resolutions import ReadsExactly, IsEqual
from screenpy_selenium.actions import Open

from libraries.api_client import ApiClient
from tasks import Login, CloseToastMessage
from tasks.asset_list_game import AddBeat, EditBeat, ExpandTitle, FavouriteFranchise, FavouriteTitle, Filter, FilterType, SetDefaultLocales, Search
from questions import ToastMessage
from questions.asset_list_game import AssetListGameHomePageData, AssetListGameFavouriteSection
from features.base_test import BaseTest


class TestFilterSearchFavoriteAndAddBeatInAssetTrackerGame(BaseTest):

    @staticmethod
    def fetch_franchises_data(
            franchises: list,
            titles: list,
            only_active_titles: bool = False,
            only_ea_titles: bool = False,
            additional_content: bool = False
    ):
        desired_franchise_ids = []
        if only_active_titles:
            desired_franchise_ids += set([item['franchiseId'] for item in titles if item['isActive']])
        if only_ea_titles:
            desired_franchise_ids += set([item['franchiseId'] for item in titles if item['isEAGame']])
        if additional_content:
            desired_franchise_ids += set([item['franchiseId'] for item in titles if item['gameObjectType'] == 'base-game'])
        if desired_franchise_ids:
            desired_franchises = list(filter(lambda franchise: franchise['id'] in set(desired_franchise_ids), franchises))
        else:
            valid_franchise_ids = set([item['franchiseId'] for item in titles])
            desired_franchises = [item for item in franchises if item['id'] in valid_franchise_ids]
        return [item['name'] for item in desired_franchises]

    def test_filter_search_favourite_and_add_beat(self, the_qa_engineer_2: AnActor):
        base_url = self.pages['ASSET_LIST_GAME_PAGE'].url
        api = ApiClient(the_qa_engineer_2, base_url)
        given(the_qa_engineer_2).attempts_to(Open.their_browser_on(base_url))
        when(the_qa_engineer_2).attempts_to(
            Login('chivu', '123456')
        )
        franchises = api.wait_for_franchises_es_request().get('franchises')
        titles = api.wait_for_titles_es_request().get('titles')
        all_franchises = sorted(self.fetch_franchises_data(franchises, titles))
        active_franchises = sorted(self.fetch_franchises_data(franchises, titles, only_active_titles=True))
        ea_franchises = sorted(self.fetch_franchises_data(franchises, titles, only_ea_titles=True))
        additional_content_franchises = sorted(self.fetch_franchises_data(franchises, titles, additional_content=True))
        # Clear default filters
        when(the_qa_engineer_2).attempts_to(
            Filter(FilterType.SHOW_ONLY_ACTIVE_TITLES, disabled=True),
            Filter(FilterType.SHOW_ONLY_EA_TITLES, disabled=True),
            Filter(FilterType.SHOW_ADDITIONAL_CONTENT, disabled=True)
        )
        # Turn On Show Only Active Titles Filter
        when(the_qa_engineer_2).attempts_to(
            Filter(FilterType.SHOW_ONLY_ACTIVE_TITLES)
        )
        then(the_qa_engineer_2).should(
            See.the(AssetListGameHomePageData("franchise", len(active_franchises)),
                    IsEqual(active_franchises))
        )
        # Turn Off Show Only Active Titles Filter
        when(the_qa_engineer_2).attempts_to(
            Filter(FilterType.SHOW_ONLY_ACTIVE_TITLES, disabled=True)
        )
        then(the_qa_engineer_2).should(
            See.the(AssetListGameHomePageData("franchise", len(all_franchises)),
                    IsEqual(all_franchises))
        )
        # Turn On Show Only EA Titles Filter
        when(the_qa_engineer_2).attempts_to(
            Filter(FilterType.SHOW_ONLY_EA_TITLES)
        )
        then(the_qa_engineer_2).should(
            See.the(AssetListGameHomePageData("franchise", len(ea_franchises)),
                    IsEqual(ea_franchises))
        )
        # Turn Off Show Only EA Titles Filter
        when(the_qa_engineer_2).attempts_to(
            Filter(FilterType.SHOW_ONLY_EA_TITLES, disabled=True)
        )
        then(the_qa_engineer_2).should(
            See.the(AssetListGameHomePageData("franchise", len(all_franchises)),
                    IsEqual(all_franchises))
        )
        # Turn On Show Additional Content Filter
        when(the_qa_engineer_2).attempts_to(
            Filter(FilterType.SHOW_ADDITIONAL_CONTENT)
        )
        then(the_qa_engineer_2).should(
            See.the(AssetListGameHomePageData("franchise", len(additional_content_franchises)),
                    IsEqual(additional_content_franchises))
        )
        # Turn Off Show Additional Content Filter
        when(the_qa_engineer_2).attempts_to(
            Filter(FilterType.SHOW_ADDITIONAL_CONTENT, disabled=True)
        )
        then(the_qa_engineer_2).should(
            See.the(AssetListGameHomePageData("franchise", len(all_franchises)),
                    IsEqual(all_franchises))
        )
        # Search Franchise and Favourite
        franchise_name = "Dillan"
        when(the_qa_engineer_2).attempts_to(
            Search(franchise_name),
            FavouriteFranchise(franchise_name)
        )
        then(the_qa_engineer_2).should(
            See.the(AssetListGameFavouriteSection("franchise"),
                    IsEqual([franchise_name]))
        )
        # Search Title and Favourite
        title = "Madden NFL 20"
        when(the_qa_engineer_2).attempts_to(
            Search(title),
            FavouriteTitle(title)
        )
        then(the_qa_engineer_2).should(
            See.the(AssetListGameFavouriteSection("title"),
                    IsEqual([title]))
        )
        # Search Title and Set Default Locales
        title = "Ernest"
        when(the_qa_engineer_2).attempts_to(
            Search(title)
        )
        then(the_qa_engineer_2).should(
            See.the(AssetListGameHomePageData("title", num_records=1),
                    IsEqual([title]))
        )
        when(the_qa_engineer_2).attempts_to(
            ExpandTitle(title),
            SetDefaultLocales("en-CA")
        )
        then(the_qa_engineer_2).should(
            See.the(ToastMessage(),
                    ReadsExactly("Successful update default locales"))
        )
        # Add Beat
        title = "Star Wars Battlefront II"
        beat_name = f"Auto_{str(uuid.uuid4())}"
        when(the_qa_engineer_2).attempts_to(
            CloseToastMessage(),
            Search(title),
            ExpandTitle(title),
            AddBeat(
                name=beat_name,
                phase="Phase 1"
            )
        )
        then(the_qa_engineer_2).should(
            See.the(ToastMessage(),
                    ReadsExactly("Beat created successfully"))
        )
        # Search Beat And Edit
        when(the_qa_engineer_2).attempts_to(
            CloseToastMessage(),
            Search(beat_name),
            EditBeat(is_evergreen=True)
        )
        then(the_qa_engineer_2).should(
            See.the(ToastMessage(),
                    ReadsExactly("Beats updated successfully"))
        )
