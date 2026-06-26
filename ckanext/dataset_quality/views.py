# encoding: utf-8
from __future__ import annotations

from typing import Any

from flask import Blueprint, jsonify, url_for

import ckan.plugins.toolkit as tk
from ckan.common import current_user

from ckanext.dataset_quality.service import build_quality_report


quality_blueprint = Blueprint("dataset_quality", __name__)


def _api_context() -> dict[str, Any]:
    return {
        "user": getattr(current_user, "name", None),
        "auth_user_obj": current_user,
        "api_version": 3,
    }


@quality_blueprint.route("/dataset/quality-report")
def quality_report_page() -> str:
    report = build_quality_report(_api_context())
    return tk.render("dataset_quality/quality_report.html", {"report": report})


@quality_blueprint.route("/api/action/quality_report", methods=["GET", "POST"])
@quality_blueprint.route("/api/3/action/quality_report", methods=["GET", "POST"])
def quality_report_api():
    if not getattr(current_user, "is_authenticated", False):
        response = {
            "help": url_for(
                "api.action",
                ver=3,
                logic_function="help_show",
                name="quality_report",
                _external=True,
            ),
            "success": False,
            "error": {
                "__type": "Authorization Error",
                "message": "Authentication required",
            },
        }
        return jsonify(response), 401

    try:
        result = tk.get_action("quality_report")(_api_context(), {})
    except tk.NotAuthorized as err:
        response = {
            "help": url_for(
                "api.action",
                ver=3,
                logic_function="help_show",
                name="quality_report",
                _external=True,
            ),
            "success": False,
            "error": {
                "__type": "Authorization Error",
                "message": str(err) or "Access denied",
            },
        }
        return jsonify(response), 403

    return (
        jsonify(
            {
                "help": url_for(
                    "api.action",
                    ver=3,
                    logic_function="help_show",
                    name="quality_report",
                    _external=True,
                ),
                "success": True,
                "result": result,
            }
        ),
        200,
    )
