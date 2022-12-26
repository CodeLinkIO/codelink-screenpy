from pytest import fixture

from ui.asset_list_game import AssetListGamePage
from ui.asset_list_non_game import AssetListNonGamePage
from ui.asset_search import AssetSearchPage
from ui.asset_upload import AssetUploadPage
from ui.channel_ready_library import ChannelReadyLibraryPage
from ui.juno_hub import JunoHubPage
from ui.photo_shoot_library import PhotoShootLibraryPage
from ui.youtub_hub import YoutubeHubPage
from utils.json_reader import deep_get


@fixture
def pages(env, env_data):
    ASSET_LIST_GAME_PAGE = AssetListGamePage(f"{get_path(env, env_data, 'asset_list_game')}")
    ASSET_LIST_NON_GAME_PAGE = AssetListNonGamePage(f"{get_path(env, env_data, 'asset_list_non_game')}")
    YOUTUBE_HUB_PAGE = YoutubeHubPage(f"{get_path(env, env_data, 'youtube_hub')}")
    ASSET_SEARCH_PAGE = AssetSearchPage(f"{get_path(env, env_data, 'asset_search')}")
    ASSET_UPLOAD_PAGE = AssetUploadPage(f"{get_path(env, env_data, 'asset_upload')}")
    JUNO_HUB_PAGE = JunoHubPage(f"{get_path(env, env_data, 'juno_hub')}")
    PHOTO_SHOOT_LIBRARY_PAGE = PhotoShootLibraryPage(f"{get_path(env, env_data, 'photo_shoot_library')}")
    CHANNEL_READY_LIBRARY_PAGE = ChannelReadyLibraryPage(f"{get_path(env, env_data, 'channel_ready_library')}")
    return locals()


def get_path(env, env_data, path):
    return deep_get(
        env_data,
        f'{env}.{path}',
        deep_get(env_data, f'default.{path}')
    )
