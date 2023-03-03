import uuid

from screenpy import AnActor, given, when, then
from screenpy.actions import See
from screenpy.resolutions import ReadsExactly, IsEqual
from screenpy_selenium.actions import Open

from enums.asset_level import AssetLevel
from tasks import Login, CloseToastMessage
from tasks.asset_list_game import AddBeat, EditBeat, ExpandTitle, FavouriteFranchise, FavouriteTitle, Filter, FilterType, SetDefaultLocales, Search
from questions import ToastMessage
from questions.asset_list_game import AssetListData, FavouriteAssetListData
from features.base_test import BaseTest


class TestFilterSearchFavoriteAndAddBeatInAssetTrackerGame(BaseTest):

    ALL_FRANCHISES = ['A Plague Tale Innocence', 'A Way Out', 'Alice', 'Anthem', 'Ao Tennis', 'Apex Legends', 'Apotheon', 'Aragami', 'Autonauts', 'Batman: Arkham', 'Battlefield', 'Beholder', 'Bejeweled', 'Blackguards', 'Bloodstained', 'Bomber Crew', 'Breathedge', 'Burnout', 'Cities Skylines', 'Command & Conquer', 'Content Hub Playground', 'Cosmic Star Heroine', 'Crashlands', 'Crawl', 'Cryptark', 'Crysis', 'Darksiders', 'Dead Cells', 'Dead In Vinland', 'Dead Space', 'Dear Esther', 'Deponia', 'Detention', 'Dillan', 'Diluvion', 'Dragon Age', 'Dungeon Keeper', 'Dungeons', 'Dungeons of Dredmor', 'Epistory', 'Farmers Dynasty', 'Farming Simulator', 'Fe', 'FIFA', 'Figment', 'Final Fantasy', 'For The King', 'Fran Bow', 'Frostpunk', 'FTL: Faster Than Light', 'Furi', 'Ghost Of A Tale', 'Gone Home', 'Hacknet', 'Halcyon 6', 'Hand of Fate', 'Highway Fixture', 'Home Behind', 'Hover', 'Hue', 'Hyper Light Drifter', 'Inside', 'Into The Breach', 'It Takes Two', 'Jade Empire', 'Judgment: Apocalypse Survival Simulation', 'Kingdom', 'Kingdoms of Amalur: Reckoning', 'Lego Star Wars', 'Legrand Legacy', 'Limbo', 'Little Misfortune', 'Lost Castle', 'Mable And The Wood', 'Mad Games Tycoon', 'Mad Max', 'Madden', 'Mass Effect', 'Medal of Honor', 'Mini Metro', 'Mirrors Edge', 'Moonlighter', 'Mr. Shifty', 'Mugsters', 'Mutant Year Zero: Road to Eden', 'Need for Speed', 'Nex Machina', 'Northgard', 'Nox', 'Opus Magnum', 'Out of the Park Baseball', 'Overcooked', 'Oxenfree', 'Peggle', 'Plants vs Zombies', 'Pony Island', 'Prison Architect', 'Project Highrise', 'Punch Club', 'Pyre', 'Rebel Galaxy', 'Renowned Explorers', 'Rime', 'Rocket Arena', 'Saboteur', 'Samorost', 'Sea of Solitude', 'Seasons After Fall', 'Shadow Tactics', 'Shantae', 'Shenzhen I/O', 'Shift', 'Shio', 'SimCity', 'Sinner: Sacrifice for Redemption', 'Slay The Spire', 'Slime-san', 'Snake Pass', 'Sparklite', 'Splasher', 'Spore', 'Star Wars', 'Star Wars Episode I: Racer', 'Star Wars: Battlefront Classic', 'Star Wars: Empire at War', 'Star Wars: Galactic Battlegrounds', 'Star Wars: Jedi Knight', 'Star Wars: Knights of the Old Republic', 'Star Wars: Rebel Assault', 'Star Wars: Rebellion', 'Star Wars: Republic Commando', 'Star Wars: Rogue Squadron 3D', 'Star Wars: Shadows of the Empire', 'Star Wars: Squadrons', 'Star Wars: Starfighter', 'Star Wars: The Force Unleashed', 'Star Wars: X-Wing', 'Stealth Bastard', 'SteamWorld', 'Sudden Strike', 'Superbowl', 'Superhot', 'Tacoma', 'Tharsis', "The Bard's Tale", 'The Book of Unwritten Tales', 'The Count Lucanor', 'The Escapists', 'The Flame in the Flood', 'The Invisible Hours', 'The Lego Movie', 'The Pillars of the Earth', 'The Sexy Brutale', 'The Sims', 'The Solus Project', 'The Surge', 'Theme Hospital', 'They Are Billions', 'This is the Police', 'This War of Mine', 'Titanfall', 'Torchlight', 'Trine', 'Tropico', 'Turmoil', 'Ultimate Chicken Horse', 'Unravel', 'Vambrace: Cold Soul', 'Vampyr', 'Voltron', 'Warhammer 40000', 'Warhammer: Chaosbane', 'Witcher', 'Worms', 'Wreckfest', 'Wuppo', "Yoku's Island Express", 'Yooka-Laylee', 'Zuma']
    ACTIVE_FRANCHISES = ['A Plague Tale Innocence', 'Battlefield', 'Command & Conquer', 'Content Hub Playground', 'Dead Space', 'Dillan', 'Dragon Age', 'FIFA', 'Madden', 'Rocket Arena', 'Star Wars', 'Superbowl', 'Voltron']
    EA_FRANCHISES = ['A Plague Tale Innocence', 'A Way Out', 'Alice', 'Anthem', 'Apex Legends', 'Batman: Arkham', 'Battlefield', 'Bejeweled', 'Burnout', 'Cities Skylines', 'Command & Conquer', 'Crysis', 'Dead Space', 'Dragon Age', 'Dungeon Keeper', 'Fe', 'FIFA', 'It Takes Two', 'Kingdoms of Amalur: Reckoning', 'Madden', 'Mass Effect', 'Medal of Honor', 'Mirrors Edge', 'Need for Speed', 'Peggle', 'Plants vs Zombies', 'Rocket Arena', 'Sea of Solitude', 'SimCity', 'Spore', 'Star Wars', 'Star Wars: Battlefront Classic', 'Star Wars: Knights of the Old Republic', 'Star Wars: Squadrons', 'Star Wars: The Force Unleashed', 'The Sims', 'Titanfall', 'Unravel', 'Voltron', 'Wreckfest', 'Zuma']

    def test_filter_search_favourite_and_add_beat(self, the_qa_engineer_2: AnActor):
        given(the_qa_engineer_2).attempts_to(Open.their_browser_on(self.pages['ASSET_LIST_GAME_PAGE'].url))
        when(the_qa_engineer_2).attempts_to(
            Login('chivu', '123456'),
            # Clear default filters
            Filter(FilterType.SHOW_ONLY_ACTIVE_TITLES, disabled=True),
            Filter(FilterType.SHOW_ONLY_EA_TITLES, disabled=True),
            Filter(FilterType.SHOW_ADDITIONAL_CONTENT, disabled=True),
            # Turn On Show Only Active Titles Filter
            Filter(FilterType.SHOW_ONLY_ACTIVE_TITLES)
        )
        then(the_qa_engineer_2).should(
            See.the(AssetListData(AssetLevel.FRANCHISE, len(self.ACTIVE_FRANCHISES)),
                    IsEqual(self.ACTIVE_FRANCHISES))
        )
        # Turn Off Show Only Active Titles Filter
        when(the_qa_engineer_2).attempts_to(
            Filter(FilterType.SHOW_ONLY_ACTIVE_TITLES, disabled=True)
        )
        then(the_qa_engineer_2).should(
            See.the(AssetListData(AssetLevel.FRANCHISE, len(self.ALL_FRANCHISES)),
                    IsEqual(self.ALL_FRANCHISES))
        )
        # Turn On Show Only EA Titles Filter
        when(the_qa_engineer_2).attempts_to(
            Filter(FilterType.SHOW_ONLY_EA_TITLES)
        )
        then(the_qa_engineer_2).should(
            See.the(AssetListData(AssetLevel.FRANCHISE, len(self.EA_FRANCHISES)),
                    IsEqual(self.EA_FRANCHISES))
        )
        # Turn Off Show Only EA Titles Filter
        when(the_qa_engineer_2).attempts_to(
            Filter(FilterType.SHOW_ONLY_EA_TITLES, disabled=True)
        )
        then(the_qa_engineer_2).should(
            See.the(AssetListData(AssetLevel.FRANCHISE, len(self.ALL_FRANCHISES)),
                    IsEqual(self.ALL_FRANCHISES))
        )
        # Turn On Show Additional Content Filter
        when(the_qa_engineer_2).attempts_to(
            Filter(FilterType.SHOW_ADDITIONAL_CONTENT)
        )
        then(the_qa_engineer_2).should(
            See.the(AssetListData(AssetLevel.FRANCHISE, len(self.ALL_FRANCHISES)),
                    IsEqual(self.ALL_FRANCHISES))
        )
        # Turn Off Show Additional Content Filter
        when(the_qa_engineer_2).attempts_to(
            Filter(FilterType.SHOW_ADDITIONAL_CONTENT, disabled=True)
        )
        then(the_qa_engineer_2).should(
            See.the(AssetListData(AssetLevel.FRANCHISE, len(self.ALL_FRANCHISES)),
                    IsEqual(self.ALL_FRANCHISES))
        )
        # Search Franchise and Favourite
        franchise_name = "Dillan"
        when(the_qa_engineer_2).attempts_to(
            Search(franchise_name),
            FavouriteFranchise(franchise_name)
        )
        then(the_qa_engineer_2).should(
            See.the(FavouriteAssetListData(AssetLevel.FRANCHISE),
                    IsEqual([franchise_name]))
        )
        # Search Title and Favourite
        title = "Madden NFL 20"
        when(the_qa_engineer_2).attempts_to(
            Search(title),
            FavouriteTitle(title)
        )
        then(the_qa_engineer_2).should(
            See.the(FavouriteAssetListData(AssetLevel.TITLE),
                    IsEqual([title]))
        )
        # Search Title and Set Default Locales
        title = "Ernest"
        when(the_qa_engineer_2).attempts_to(
            Search(title)
        )
        then(the_qa_engineer_2).should(
            See.the(AssetListData(AssetLevel.TITLE, num_records=1),
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
