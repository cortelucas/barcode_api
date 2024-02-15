from flask import Blueprint, request, jsonify
from src.views.http_types import HttpRequest
from src.views.tag_creator_view import TagCreatorView
from src.erros.error_handler import handle_errors

tag_routes_bp = Blueprint("tag_routes", __name__)


@tag_routes_bp.route("/tags", methods=["post"])
def create_tag():
    response = None
    try:
        tag_creator_view = TagCreatorView()
        http_request = HttpRequest(body=request.json)

        response = tag_creator_view.validate_and_create(http_request)
    except Exception as error:
        response = handle_errors(error)

    return jsonify(response.body), response.status_code
