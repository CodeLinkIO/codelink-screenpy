from pytest import fixture

from ui.asset_list_game import AssetListGamePage
from ui.asset_list_non_game import AssetListNonGamePage
from ui.asset_search import AssetSearchPage
from ui.asset_upload import AssetUploadPage
from ui.channel_ready_library import ChannelReadyLibraryPage
from ui.juno_hub import JunoHubPage
from ui.photo_shoot_library import PhotoShootLibraryPage
from ui.youtub_hub import YoutubeHubPage
from ui.login import LoginPage
from utils.json_reader import get_value_or_default
from globals.constants import *


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
    LOGIN_PAGE = LoginPage(f"{get_path(env, env_data, 'login')}")
    return locals()


def get_path(env, env_data, path):
    return get_value_or_default(
        env_data,
        f'{env}.{path}',
        get_value_or_default(env_data, f'default.{path}')
    )
