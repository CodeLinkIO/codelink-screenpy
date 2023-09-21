from datetime import datetime

from screenpy import Actor
from screenpy.pacing import beat

from enums import MasterAssetTableAttribute
from questions.elastic_search.nuxeo_es_search import NuxeoEsSearch


class GetMasterAssetsWithoutYouTubeVersion:

    @staticmethod
    def get_master_assets_with_youtube_plan_channel_payload(
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
                            "terms": {
                                "as:planned_channels": [
                                    "youtube-owned",
                                    "youtube-paid"
                                ]
                            }
                        },
                        {
                            "term": {
                                "ecm:mixinType": "Master"
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
                "ecm:uuid"
            ]
        }

    @staticmethod
    def get_master_assets_without_youtube_version_payload(
            uuids: list
    ):
        return {
            "query": {
                "bool": {
                    "must": [
                        {
                            "terms": {
                                "ecm:parentId": uuids
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

    @staticmethod
    def get_beat_info_payload(
            beat_ids: list
    ):
        return {
            "query": {
                "bool": {
                    "must": [
                        {
                            "terms": {
                                "ecm:uuid": beat_ids
                            }
                        }
                    ]
                }
            },
            "_source": [
                "ecm:name",
                "ecm:uuid"
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

    def get_uuids_master_assets_with_youtube_plan_channel(self, the_actor: Actor):
        assets_with_youtube_plan_channel_resp = NuxeoEsSearch(
            path=self.path,
            params=self.get_master_assets_with_youtube_plan_channel_payload([self.game_id]),
            username=self.username,
            password=self.password
        ).answered_by(the_actor)
        uuids = []
        for item in assets_with_youtube_plan_channel_resp['hits']['hits']:
            uuids.append(item['_source']['ecm:uuid'])
        return list(set(uuids))

    def get_ids_master_assets_without_youtube_version(self, uuids: list, the_actor: Actor):
        resp = NuxeoEsSearch(
            path=self.path,
            params=self.get_master_assets_without_youtube_version_payload(uuids),
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
        headers = [
            MasterAssetTableAttribute.MASTER_NAME,
            MasterAssetTableAttribute.VOLTRON_ID,
            MasterAssetTableAttribute.BEAT,
            MasterAssetTableAttribute.GO_LIVE_DATE
        ]

        master_name_list = []
        voltron_id_list = []
        live_date_list = []
        beat_name_list = []
        beat_list = {}

        for item in resp['hits']['hits']:
            source = item['_source']
            master_name_list.append(source.get('dc:title'))
            voltron_id_list.append(source.get('as:asset_id'))
            live_date = source.get('asm:live_date', None)
            if live_date:
                live_date = datetime.strptime(
                    live_date.split(".")[0], "%Y-%m-%dT%H:%M:%S"
                ).strftime("%b %d, %Y")
            live_date_list.append(live_date or "-")
            beat_list.update({
                source.get('as:asset_id'): source.get('asm:beat')
            })
        beats_info = self.get_beats_info(list(set(beat_list.values())), the_actor)
        for voltron_id in voltron_id_list:
            beat_name_list.append(beats_info.get(beat_list.get(voltron_id)))
        for i in range(len(master_name_list)):
            data.append(dict(zip(headers, [master_name_list[i], voltron_id_list[i], beat_name_list[i], live_date_list[i]])))
        return data

    def get_beats_info(self, beat_ids: list, the_actor: Actor):
        resp = NuxeoEsSearch(
            path=self.path,
            params=self.get_beat_info_payload(beat_ids),
            username=self.username,
            password=self.password
        ).answered_by(the_actor)
        data = {}
        for item in resp['hits']['hits']:
            data.update({
                item.get('_source').get('ecm:uuid'): item.get('_source').get('ecm:name')
            })
        return data

    @beat("{} examines master assets data by YouTube version.")
    def answered_by(self, the_actor: Actor):
        uuids_master_assets_with_youtube_plan_channel = self.get_uuids_master_assets_with_youtube_plan_channel(the_actor)
        ids_master_assets_without_youtube_version = self.get_ids_master_assets_without_youtube_version(
            uuids_master_assets_with_youtube_plan_channel, the_actor
        )
        parent_ids_version_assets_without_youtube_version = list(
            set(uuids_master_assets_with_youtube_plan_channel) - set(ids_master_assets_without_youtube_version)
        )
        master_assets_without_youtube_version = self.get_master_assets_info(
            parent_ids_version_assets_without_youtube_version,
            the_actor
        )
        return master_assets_without_youtube_version
