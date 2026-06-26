# encoding: utf-8
from __future__ import annotations

from ckan.types import Context, DataDict


def quality_report(context: Context, data_dict: DataDict) -> dict[str, str | bool]:
    user = context.get("user")
    auth_user = context.get("auth_user_obj")

    is_authenticated = bool(user)
    if auth_user is not None:
        is_authenticated = bool(getattr(auth_user, "is_authenticated", is_authenticated))

    if not is_authenticated:
        return {"success": False, "msg": "Authentication required"}

    return {"success": True}
