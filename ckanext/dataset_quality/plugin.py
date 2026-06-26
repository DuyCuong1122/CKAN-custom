# encoding: utf-8
from __future__ import annotations

import json
from typing import Any, Callable

from ckan.common import CKANConfig

import ckan.plugins as plugins
import ckan.plugins.toolkit as tk

from ckanext.dataset_quality.logic import action, auth
from ckanext.dataset_quality.service import (
    calculate_dataset_quality,
    enrich_dataset_with_quality,
    get_quality_badge_class,
)
from ckanext.dataset_quality.views import quality_blueprint


class DatasetQualityPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IPackageController, inherit=True)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IBlueprint)
    plugins.implements(plugins.IActions)
    plugins.implements(plugins.IAuthFunctions)

    def update_config(self, config: CKANConfig) -> None:
        tk.add_template_directory(config, "templates")

    def get_helpers(self) -> dict[str, Callable[..., Any]]:
        return {
            "calculate_dataset_quality": calculate_dataset_quality,
            "quality_badge_class": get_quality_badge_class,
        }

    def get_blueprint(self):
        return quality_blueprint

    def get_actions(self):
        return action.get_actions()

    def get_auth_functions(self):
        return {"quality_report": auth.quality_report}

    def before_dataset_index(self, pkg_dict: dict[str, Any]) -> dict[str, Any]:
        validated_data = pkg_dict.get("validated_data_dict")
        source_dataset = pkg_dict
        if validated_data:
            source_dataset = json.loads(validated_data)

        score = calculate_dataset_quality(source_dataset)
        pkg_dict["extras_quality_score"] = str(score)
        pkg_dict["extras_quality_high"] = "true" if score >= 80 else "false"
        pkg_dict["extras_quality_medium"] = "true" if score >= 50 else "false"
        pkg_dict["extras_quality_low"] = "true" if score < 50 else "false"
        return pkg_dict

    def before_dataset_search(self, search_params: dict[str, Any]) -> dict[str, Any]:
        extras = search_params.get("extras", {})
        selected_quality = extras.get("ext_quality")
        if isinstance(selected_quality, list):
            selected_quality = selected_quality[-1] if selected_quality else None
        filter_map = {
            "high": 'extras_quality_high:"true"',
            "medium": 'extras_quality_medium:"true"',
            "low": 'extras_quality_low:"true"',
        }

        if selected_quality in filter_map:
            search_params["fq"] = (
                f'{search_params.get("fq", "").strip()} +{filter_map[selected_quality]}'
            ).strip()

        return search_params

    def after_dataset_show(
        self, context: dict[str, Any], pkg_dict: dict[str, Any]
    ) -> dict[str, Any]:
        return enrich_dataset_with_quality(pkg_dict)

    def after_dataset_search(
        self, search_results: dict[str, Any], search_params: dict[str, Any]
    ) -> dict[str, Any]:
        for dataset in search_results.get("results", []):
            enrich_dataset_with_quality(dataset)
        return search_results
