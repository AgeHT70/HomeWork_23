from typing import Any

from marshmallow import Schema, fields, validates_schema, ValidationError

from functions import CMDS


class RequestSchema(Schema):
    cmd = fields.Str(required=True)
    value = fields.Str()

    @validates_schema
    def check_all_cmd(self, values: dict[str, str], *args: Any,
                      **kwargs: Any) -> None:
        if values['cmd'] not in CMDS.keys():
            raise ValidationError('check command')


class BatchRequestSchema(Schema):
    file_name = fields.Str(required=True)
    queries = fields.Nested(RequestSchema, many=True)
