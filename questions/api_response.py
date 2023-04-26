import gzip
import io
import json

from screenpy import Actor
from screenpy.pacing import beat

from screenpy_selenium.abilities import BrowseTheWeb


class ApiResponse:

    def __init__(self, path: str, timeout: int = 10):
        self.path = path
        self.timeout = timeout

    @beat("{} examines the response of the request with path `{path}` for {timeout} seconds.")
    def answered_by(self, the_actor: Actor) -> dict:
        driver = the_actor.ability_to(BrowseTheWeb).browser
        request = driver.wait_for_request(self.path, self.timeout)
        buf = io.BytesIO(request.response.body)
        gzip_f = gzip.GzipFile(fileobj=buf)
        return json.loads(gzip_f.read().decode("utf-8"))
