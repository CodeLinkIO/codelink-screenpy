from pytest import fixture

from ui import AssetListGamePage, AssetListNonGamePage, AssetSearchPage, AssetUploadPage, ChannelReadyLibraryPage, JunoHubPage, PhotoShootLibraryPage, YoutubeHubPage, LoginPage
from utils.json_reader import get_value_or_default
from globals.constants import ASSET_SEARCH, ASSET_UPLOAD, ASSET_LIST_GAME, ASSET_LIST_NON_GAME, PHOTO_SHOOT_LIBRARY, CHANNEL_READY_LIBRARY, JUNO_HUB, YOUTUBE_HUB, LOGIN


@fixture
def pages(env, env_data):
    ASSET_LIST_GAME_PAGE = AssetListGamePage(f"{get_path(env, env_data, ASSET_LIST_GAME)}")
    ASSET_LIST_NON_GAME_PAGE = AssetListNonGamePage(f"{get_path(env, env_data, ASSET_LIST_NON_GAME)}")
    YOUTUBE_HUB_PAGE = YoutubeHubPage(f"{get_path(env, env_data, YOUTUBE_HUB)}")
    ASSET_SEARCH_PAGE = AssetSearchPage(f"{get_path(env, env_data, ASSET_SEARCH)}")
    ASSET_UPLOAD_PAGE = AssetUploadPage(f"{get_path(env, env_data, ASSET_UPLOAD)}")
    JUNO_HUB_PAGE = JunoHubPage(f"{get_path(env, env_data, JUNO_HUB)}")
    PHOTO_SHOOT_LIBRARY_PAGE = PhotoShootLibraryPage(f"{get_path(env, env_data, PHOTO_SHOOT_LIBRARY)}")
    CHANNEL_READY_LIBRARY_PAGE = ChannelReadyLibraryPage(f"{get_path(env, env_data, CHANNEL_READY_LIBRARY)}")
    LOGIN_PAGE = LoginPage(f"{get_path(env, env_data, LOGIN)}")
    return locals()


def get_path(env, env_data, path):
    return get_value_or_default(
        env_data,
        f'{env}.{path}',
        get_value_or_default(env_data, f'default.{path}')
    )
