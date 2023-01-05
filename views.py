import os
from typing import Optional, Iterable

from flask import Blueprint, request, jsonify, Response
from marshmallow import ValidationError

from functions import execute
from models import BatchRequestSchema

main_bp = Blueprint("perform_query", __name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@main_bp.route("/perform_query", methods=["POST"])
def perform_query() -> Response:
    if request.json is not None:
        try:
            validated_data: dict = BatchRequestSchema().load(
                data=request.json)
        except ValidationError as e:
            return Response(response=e.messages, status=400)

        queries: list[dict[str, str]] = validated_data["queries"]

        file_name = os.path.join(DATA_DIR, validated_data['file_name'])

        result: Optional[Iterable[str]] = None

        for query in queries:
            result = execute(
                cmd=query['cmd'],
                value=query['value'],
                filename=file_name,
                data=result
            )

        return jsonify(result)
    else:
        return Response(response="Bad request", status=400)
