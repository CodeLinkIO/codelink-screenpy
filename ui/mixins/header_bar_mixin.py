from screenpy_selenium import Target


class HeaderBarMixin:

    HEADER_MENU = Target.the('Header Menu').located_by("[class^='HeaderMenu']")
    ASSET_LIST_GAME_MENU_ITEM = Target.the('Asset list: Game Menu Item').located_by("[href*='tracker']")
    ASSET_LIST_NON_GAME_MENU_ITEM = Target.the('Asset list: Non-Game Menu Item').located_by("[href*='list']")
    ASSET_UPLOAD_MENU_ITEM = Target.the('Asset Upload Menu Item').located_by("[href*='upload']")
    ASSET_SEARCH_MENU_ITEM = Target.the('Asset Search Menu Item').located_by("[href*='search']")
    JUNO_HUB_MENU_ITEM = Target.the('Juno Hub Menu Item').located_by("[href*='juno']")
    YOUTUBE_HUB_MENU_ITEM = Target.the('Youtube Hub Menu Item').located_by("[href*='youtube']")
