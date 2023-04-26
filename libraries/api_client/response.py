import typing
from dataclasses import dataclass

from requests import Response


@dataclass
class ApiResponse:
    raw: Response
    code: int
    error: typing.Optional[str] = None
    object: typing.Optional[typing.Any] = None
