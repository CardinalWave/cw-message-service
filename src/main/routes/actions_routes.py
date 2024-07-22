from flask import Blueprint, request, jsonify
from src.main.adapters.request_adapter import request_adapter
from src.main.composers.actions.join import join_composer
from src.main.composers.actions.send import send_composer
from src.main.composers.actions.leave import leave_composer


action_route_bp = Blueprint("action_routes", __name__)


@action_route_bp.route("/chat/join", methods=["POST"])
def join():
    http_response = request_adapter(request, join_composer())
    return jsonify(http_response.body), http_response.status_code


@action_route_bp.route("/chat/send", methods=["POST"])
def send():
    http_response = request_adapter(request, send_composer())
    return jsonify(http_response.body), http_response.status_code


@action_route_bp.route("/chat/leave", methods=["POST"])
def leave():
    http_response = request_adapter(request, leave_composer())
    return jsonify(http_response.body), http_response.status_code
