from screenpy import Actor
from screenpy.pacing import beat

from libraries.api_client import ApiClient


class NuxeoEsSearch:

    def __init__(
            self,
            path: str,
            params: dict,
            username: str,
            password: str,
            search_all: bool = True,
            **headers
    ):
        self.path = path
        self.params = params
        self.username = username
        self.password = password
        self.search_all = search_all
        self.headers = dict(headers)

    def search(self, the_actor: Actor) -> dict:
        api = ApiClient(the_actor, self.path, **self.headers)
        resp = api.post(
            f"{self.path}/nuxeo/site/es/nuxeo/_search",
            params=self.params,
            auth=(self.username, self.password)
        )
        assert resp.error is None, f'Error on NuxeoEsSearch request: {resp.error}'
        return resp.object

    @beat("{} examines the Nuxeo search.")
    def answered_by(self, the_actor: Actor) -> dict:
        resp = self.search(the_actor)
        if self.search_all:
            self.params.update(size=resp['hits']['total'])
            resp = self.search(the_actor)
        return resp
