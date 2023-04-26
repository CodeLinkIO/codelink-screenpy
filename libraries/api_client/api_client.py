import json
import traceback
import logging
import requests
from requests_toolbelt.utils import dump

from screenpy import Actor

from .response import ApiResponse
from .exceptions import ApiClientError
from utils.json_encoder import json_dump


class ApiClient:
    OK_STATUS_CODES = (200, 201, 204, )
    DEFAULT_TIMEOUT = 10
    DEFAULT_HEADERS = {
        "Content-Type": "application/json"
    }

    def __init__(
            self,
            the_actor: Actor,
            base_url: str = None,
    ):
        self.base_url = base_url
        self.the_actor = the_actor
        self.headers = self.DEFAULT_HEADERS
        self.session = None
        self.prepare_session()

    def prepare_session(self):
        self.session = requests.session()
        self.session.headers.update(self.headers)

    def assemble_path(self, route: str) -> str:
        return f"{self.base_url.replace('//', '//api-')}api/{route}"

    def _process_response(
            self,
            raw_response: requests.Response
    ) -> ApiResponse:
        data = dump.dump_all(raw_response)
        logging.debug(f"RAW: {data.decode('utf-8')}")
        error_msg = None
        if raw_response.status_code not in self.OK_STATUS_CODES:
            try:
                error_msg = raw_response.json()['error']
            except (KeyError, UnicodeDecodeError, json.JSONDecodeError):
                error_msg = raw_response.text
                traceback.print_exc()
        return ApiResponse(
            raw=raw_response,
            code=raw_response.status_code,
            object=raw_response.json(),
            error=error_msg
        )

    def _request(
            self,
            method: str,
            *args,
            **kwargs
    ):
        r = None
        try:
            r = getattr(self.session, method)(*args, **kwargs)
            return self._process_response(r)
        except requests.exceptions.RequestException as e:
            raise ApiClientError(f"{e}\n{r and r.content}")
        except AttributeError as e:
            raise ApiClientError(f"Invalid Method Specified: {method}\n{e}")

    def get(self, path: str, params: dict = None):
        return self._request('get', path, params=params)

    def post(self, path: str, params: dict = None):
        return self._request('post', path, data=json_dump(params))
