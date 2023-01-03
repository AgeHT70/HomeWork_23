import os

from flask import Blueprint, request, abort, jsonify

from functions import execute
from models import BatchRequestSchema

main_bp = Blueprint("perform_query", __name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@main_bp.route("/perform_query", methods=["POST"])
def perform_query():
    data = request.json
    validated_data = BatchRequestSchema().load(data)
    queries = validated_data["queries"]

    file_name = os.path.join(DATA_DIR, validated_data['file_name'])

    result = None
    for query in queries:
        result = execute(
            cmd=query['cmd'],
            value=query['value'],
            filename=file_name,
            data=result
        )

    return jsonify(result)
