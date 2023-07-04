import uuid

from pytest_check import check
from screenpy import AnActor, given, then, when
from screenpy.actions import MakeNote, See
from screenpy.directions import noted_under
from screenpy.resolutions import IsEqual, ReadsExactly
from screenpy_selenium.actions import Open

from features.base_test import BaseTest
from libraries.api_client.routes import Routes
from questions import ApiResponse, ToastMessage
from questions.asset_list_game import (AssetListGameFavouriteSection,
                                       AssetListGameHomePageData,
                                       FranchisesFilteredData)
from tasks import CloseToastMessage, Login
from tasks.asset_list_game import (AddBeat, EditBeat, ExpandTitle,
                                   FavouriteFranchise, FavouriteTitle, Filter,
                                   FilterType, Search, SetDefaultLocales)


class TestFilterSearchFavoriteAndAddBeatInAssetTrackerGame(BaseTest):

    def test_filter_search_favourite_and_add_beat(self, the_qa_engineer_2: AnActor):
        given(the_qa_engineer_2).was_able_to(
            Open.their_browser_on(self.pages['ASSET_LIST_GAME_PAGE'].url),
            Login('chivu', '123456'),
            MakeNote.of_the(ApiResponse(Routes.FRANCHISES_ES)).as_("franchises"),
            MakeNote.of_the(ApiResponse(Routes.TITLES_ES)).as_("titles")
        )
        when(the_qa_engineer_2).attempts_to(
            MakeNote.of_the(
                FranchisesFilteredData(noted_under("franchises"), noted_under("titles"))
            ).as_("all_franchises"),
            MakeNote.of_the(
                FranchisesFilteredData(noted_under("franchises"), noted_under("titles"), only_active_titles=True)
            ).as_("active_franchises"),
            MakeNote.of_the(
                FranchisesFilteredData(noted_under("franchises"), noted_under("titles"), only_ea_titles=True)
            ).as_("ea_franchises"),
            MakeNote.of_the(
                FranchisesFilteredData(noted_under("franchises"), noted_under("titles"), additional_content=True)
            ).as_("additional_content_franchises")
        )
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
        with check:
            then(the_qa_engineer_2).should(
                See.the(AssetListGameHomePageData("franchise", len(noted_under("active_franchises"))),
                        IsEqual(noted_under("active_franchises")))
            )
        # Turn Off Show Only Active Titles Filter
        when(the_qa_engineer_2).attempts_to(
            Filter(FilterType.SHOW_ONLY_ACTIVE_TITLES, disabled=True)
        )
        with check:
            then(the_qa_engineer_2).should(
                See.the(AssetListGameHomePageData("franchise", len(noted_under("all_franchises"))),
                        IsEqual(noted_under("all_franchises")))
            )
        # Turn On Show Only EA Titles Filter
        when(the_qa_engineer_2).attempts_to(
            Filter(FilterType.SHOW_ONLY_EA_TITLES)
        )
        with check:
            then(the_qa_engineer_2).should(
                See.the(AssetListGameHomePageData("franchise", len(noted_under("ea_franchises"))),
                        IsEqual(noted_under("ea_franchises")))
            )
        # Turn Off Show Only EA Titles Filter
        when(the_qa_engineer_2).attempts_to(
            Filter(FilterType.SHOW_ONLY_EA_TITLES, disabled=True)
        )
        with check:
            then(the_qa_engineer_2).should(
                See.the(AssetListGameHomePageData("franchise", len(noted_under("all_franchises"))),
                        IsEqual(noted_under("all_franchises")))
            )
        # Turn On Show Additional Content Filter
        when(the_qa_engineer_2).attempts_to(
            Filter(FilterType.SHOW_ADDITIONAL_CONTENT)
        )
        with check:
            then(the_qa_engineer_2).should(
                See.the(AssetListGameHomePageData("franchise", len(noted_under("additional_content_franchises"))),
                        IsEqual(noted_under("additional_content_franchises")))
            )
        # Turn Off Show Additional Content Filter
        when(the_qa_engineer_2).attempts_to(
            Filter(FilterType.SHOW_ADDITIONAL_CONTENT, disabled=True)
        )
        with check:
            then(the_qa_engineer_2).should(
                See.the(AssetListGameHomePageData("franchise", len(noted_under("all_franchises"))),
                        IsEqual(noted_under("all_franchises")))
            )
        # Search Franchise and Favourite
        franchise_name = "Dillan"
        when(the_qa_engineer_2).attempts_to(
            Search(franchise_name),
            FavouriteFranchise(franchise_name)
        )
        with check:
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
        with check:
            then(the_qa_engineer_2).should(
                See.the(AssetListGameFavouriteSection("title"),
                        IsEqual([title]))
            )
        # Search Title and Set Default Locales
        title = "Ernest"
        when(the_qa_engineer_2).attempts_to(
            Search(title)
        )
        with check:
            then(the_qa_engineer_2).should(
                See.the(AssetListGameHomePageData("title", num_records=1),
                        IsEqual([title]))
            )
        when(the_qa_engineer_2).attempts_to(
            ExpandTitle(title),
            SetDefaultLocales("en-CA")
        )
        with check:
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
        with check:
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
        with check:
            then(the_qa_engineer_2).should(
                See.the(ToastMessage(),
                        ReadsExactly("Beats updated successfully"))
            )
