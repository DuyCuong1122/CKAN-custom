# encoding: utf-8
from __future__ import annotations

from ckan.types import Action, Context, DataDict

import ckan.plugins.toolkit as tk

from ckanext.dataset_quality.service import build_quality_report


def get_actions() -> dict[str, Action]:
    return {"quality_report": quality_report}


@tk.side_effect_free
def quality_report(context: Context, data_dict: DataDict) -> dict[str, float | int]:
    tk.check_access("quality_report", context, data_dict)

    report = build_quality_report(dict(context))
    return {
        "total_datasets": report["total_datasets"],
        "average_quality_score": report["average_quality_score"],
    }
