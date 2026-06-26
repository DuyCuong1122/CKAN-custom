# encoding: utf-8
from __future__ import annotations

from typing import Any, Iterable, Mapping

from ckan import model
import ckan.plugins.toolkit as tk


HIGH_QUALITY_LABEL = "High Quality"
MEDIUM_QUALITY_LABEL = "Medium Quality"
LOW_QUALITY_LABEL = "Low Quality"


def _as_text(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def _as_list(value: Any) -> list[Any]:
    if not value:
        return []
    if isinstance(value, list):
        return value
    if isinstance(value, tuple):
        return list(value)
    return [value]


def calculate_dataset_quality(dataset: Mapping[str, Any] | None) -> int:
    dataset = dataset or {}

    score = 0

    if _as_text(dataset.get("title")):
        score += 20

    note = _as_text(dataset.get("note") or dataset.get("notes"))
    if len(note) > 100:
        score += 20

    if _as_list(dataset.get("tags")):
        score += 15

    if _as_list(dataset.get("resources")):
        score += 20

    if _as_text(dataset.get("owner_org")):
        score += 15

    if _as_text(dataset.get("license_id")):
        score += 10

    return min(int(score), 100)


def get_quality_filters(score: int) -> list[str]:
    filters = []
    if score >= 80:
        filters.append(HIGH_QUALITY_LABEL)
    if score >= 50:
        filters.append(MEDIUM_QUALITY_LABEL)
    if score < 50:
        filters.append(LOW_QUALITY_LABEL)
    return filters


def get_quality_badge_class(score: int) -> str:
    if score <= 50:
        return "bg-danger"
    if score <= 80:
        return "bg-warning text-dark"
    return "bg-success"


def enrich_dataset_with_quality(dataset: dict[str, Any]) -> dict[str, Any]:
    score = calculate_dataset_quality(dataset)
    dataset["quality_score"] = score
    dataset["quality_filters"] = get_quality_filters(score)
    return dataset


def _dataset_title(dataset: Mapping[str, Any]) -> str:
    return (
        _as_text(dataset.get("title"))
        or _as_text(dataset.get("name"))
        or _as_text(dataset.get("id"))
        or "Untitled dataset"
    )


def _organization_title(dataset: Mapping[str, Any]) -> str:
    organization = dataset.get("organization")
    if isinstance(organization, Mapping):
        return (
            _as_text(organization.get("title"))
            or _as_text(organization.get("name"))
            or "-"
        )
    return "-"


def _iter_visible_dataset_names(
    context: dict[str, Any], batch_size: int = 1000
) -> Iterable[str]:
    offset = 0

    while True:
        dataset_names = [
            dataset_name
            for (dataset_name,) in (
                model.Session.query(model.Package.name)
                .filter(model.Package.state == "active")
                .filter(model.Package.type == "dataset")
                .order_by(model.Package.name)
                .limit(batch_size)
                .offset(offset)
                .all()
            )
        ]
        if not dataset_names:
            break

        for dataset_name in dataset_names:
            yield dataset_name

        offset += len(dataset_names)


def _iter_visible_datasets(
    context: dict[str, Any], batch_size: int = 1000
) -> Iterable[dict[str, Any]]:
    package_show = tk.get_action("package_show")

    for dataset_name in _iter_visible_dataset_names(context, batch_size=batch_size):
        try:
            # Always read the latest dataset state from the database instead of
            # relying on possibly stale search-index projections.
            yield package_show(
                {
                    **context,
                    "use_cache": False,
                },
                {
                    "id": dataset_name,
                },
            )
        except (tk.ObjectNotFound, tk.NotAuthorized):
            continue


def build_quality_report(
    context: dict[str, Any], batch_size: int = 1000
) -> dict[str, Any]:
    total_datasets = 0
    total_score = 0
    lowest_quality_datasets: list[dict[str, Any]] = []

    for dataset in _iter_visible_datasets(context, batch_size=batch_size):
        score = calculate_dataset_quality(dataset)
        total_datasets += 1
        total_score += score

        lowest_quality_datasets.append(
            {
                "id": dataset.get("id"),
                "name": dataset.get("name"),
                "title": _dataset_title(dataset),
                "score": score,
                "organization": _organization_title(dataset),
                "metadata_modified": dataset.get("metadata_modified"),
            }
        )
        lowest_quality_datasets.sort(
            key=lambda item: (
                item["score"],
                item["title"].lower(),
            )
        )
        lowest_quality_datasets = lowest_quality_datasets[:10]

    average_score = round(total_score / total_datasets, 1) if total_datasets else 0.0

    return {
        "total_datasets": total_datasets,
        "average_quality_score": average_score,
        "lowest_quality_datasets": lowest_quality_datasets,
    }
