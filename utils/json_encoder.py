import json
from enum import Enum
from decimal import Decimal
from datetime import datetime


class CustomJSONEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, Decimal):
            return round(float(obj), 2)
        elif isinstance(obj, Enum):
            return obj.value
        elif isinstance(obj, datetime):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)


def json_dump(data: dict) -> str:
    return json.dumps(data, cls=CustomJSONEncoder)
