from screenpy import Actor
from screenpy.pacing import beat

from enums import MasterAssetTableAttribute
from questions.elastic_search.nuxeo_es_search import NuxeoEsSearch


class GetMasterAssetsWithYouTubeVersion:

    @staticmethod
    def get_version_assets_with_youtube_channel_payload(
            game_ids: list
    ):
        return {
            "query": {
                "bool": {
                    "must": [
                        {
                            "terms": {
                                "asm:game": game_ids
                            }
                        },
                        {
                            "term": {
                                "ecm:mixinType": "Version"
                            }
                        },
                        {
                            "term": {
                                "as:youtube_workflow": True
                            }
                        },
                        {
                            "term": {
                                "ecm:isTrashed": False
                            }
                        }
                    ]
                }
            },
            "_source": [
                "ecm:parentId"
            ]
        }

    @staticmethod
    def get_master_assets_info_payload(
            parent_ids: list
    ):
        return {
            "query": {
                "bool": {
                    "must": [
                        {
                            "terms": {
                                "ecm:uuid": parent_ids
                            }
                        }
                    ]
                }
            },
            "_source": [
                "dc:title",
                "as:asset_id",
                "asm:live_date",
                "asm:beat"
            ]
        }

    def __init__(
            self,
            path: str,
            username: str,
            password: str,
            game_id: str
    ):
        self.path = path
        self.username = username
        self.password = password
        self.game_id = game_id
        self.uuids = []

    def get_parent_ids_version_assets_with_youtube_channel(self, the_actor: Actor) -> list:
        resp = NuxeoEsSearch(
            path=self.path,
            params=self.get_version_assets_with_youtube_channel_payload([self.game_id]),
            username=self.username,
            password=self.password
        ).answered_by(the_actor)
        parent_ids = []
        for item in resp['hits']['hits']:
            parent_ids.append(item['_source']['ecm:parentId'])
        return list(set(parent_ids))

    def get_master_assets_info(self, parent_ids: list, the_actor: Actor):
        resp = NuxeoEsSearch(
            path=self.path,
            params=self.get_master_assets_info_payload(parent_ids),
            username=self.username,
            password=self.password
        ).answered_by(the_actor)
        data = []
        headers = [MasterAssetTableAttribute.MASTER_NAME, MasterAssetTableAttribute.VOLTRON_ID]
        for item in resp['hits']['hits']:
            source = item['_source']
            data.append(dict(zip(headers, [source.get('dc:title').strip(), source.get('as:asset_id')])))
        return data

    @beat("{} examines master assets data with YouTube version.")
    def answered_by(self, the_actor: Actor):
        parent_ids = self.get_parent_ids_version_assets_with_youtube_channel(the_actor)
        master_assets_with_youtube_version = self.get_master_assets_info(parent_ids, the_actor)
        return master_assets_with_youtube_version
