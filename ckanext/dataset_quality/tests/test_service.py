# encoding: utf-8

from ckanext.dataset_quality import service
from ckanext.dataset_quality.service import build_quality_report, calculate_dataset_quality


def test_calculate_dataset_quality_empty_dataset():
    assert calculate_dataset_quality({}) == 0


def test_calculate_dataset_quality_full_dataset():
    dataset = {
        "title": "Population Data",
        "note": "x" * 120,
        "tags": [{"name": "population"}],
        "resources": [{"url": "https://example.com/data.csv"}],
        "owner_org": "org-id",
        "license_id": "cc-by",
    }

    assert calculate_dataset_quality(dataset) == 100


def test_calculate_dataset_quality_missing_title():
    dataset = {
        "note": "x" * 120,
        "tags": [{"name": "population"}],
        "resources": [{"url": "https://example.com/data.csv"}],
        "owner_org": "org-id",
        "license_id": "cc-by",
    }

    assert calculate_dataset_quality(dataset) == 80


def test_calculate_dataset_quality_missing_note():
    dataset = {
        "title": "Population Data",
        "tags": [{"name": "population"}],
        "resources": [{"url": "https://example.com/data.csv"}],
        "owner_org": "org-id",
        "license_id": "cc-by",
    }

    assert calculate_dataset_quality(dataset) == 80


def test_calculate_dataset_quality_missing_tags():
    dataset = {
        "title": "Population Data",
        "note": "x" * 120,
        "resources": [{"url": "https://example.com/data.csv"}],
        "owner_org": "org-id",
        "license_id": "cc-by",
    }

    assert calculate_dataset_quality(dataset) == 85


def test_calculate_dataset_quality_missing_resources():
    dataset = {
        "title": "Population Data",
        "note": "x" * 120,
        "tags": [{"name": "population"}],
        "owner_org": "org-id",
        "license_id": "cc-by",
    }

    assert calculate_dataset_quality(dataset) == 80


def test_calculate_dataset_quality_missing_organization():
    dataset = {
        "title": "Population Data",
        "note": "x" * 120,
        "tags": [{"name": "population"}],
        "resources": [{"url": "https://example.com/data.csv"}],
        "license_id": "cc-by",
    }

    assert calculate_dataset_quality(dataset) == 85


def test_calculate_dataset_quality_missing_license():
    dataset = {
        "title": "Population Data",
        "note": "x" * 120,
        "tags": [{"name": "population"}],
        "resources": [{"url": "https://example.com/data.csv"}],
        "owner_org": "org-id",
    }

    assert calculate_dataset_quality(dataset) == 90


def test_build_quality_report_uses_latest_package_show_data(monkeypatch):
    class FakeQuery:
        def __init__(self):
            self._offset = 0

        def filter(self, *_args, **_kwargs):
            return self

        def order_by(self, *_args, **_kwargs):
            return self

        def limit(self, *_args, **_kwargs):
            return self

        def offset(self, value):
            self._offset = value
            return self

        def all(self):
            if self._offset == 0:
                return [("dataset-a",), ("dataset-b",)]
            return []

    class FakeSession:
        def query(self, *_args, **_kwargs):
            return FakeQuery()

    def fake_get_action(name):
        if name == "package_search":
            raise AssertionError("build_quality_report should not use package_search")

        if name == "package_show":
            def package_show(_context, data_dict):
                datasets = {
                    "dataset-a": {
                        "id": "dataset-a-id",
                        "name": "dataset-a",
                        "title": "Dataset A",
                        "note": "x" * 120,
                        "tags": [{"name": "quality"}],
                        "resources": [{"url": "https://example.com/a.csv"}],
                        "owner_org": "org-a",
                        "organization": {"title": "Org A"},
                        "license_id": "cc-by",
                        "metadata_modified": "2026-06-26T10:00:00.000000",
                    },
                    "dataset-b": {
                        "id": "dataset-b-id",
                        "name": "dataset-b",
                        "title": "Dataset B",
                        "metadata_modified": "2026-06-26T11:00:00.000000",
                    },
                }
                assert _context["use_cache"] is False
                return datasets[data_dict["id"]]

            return package_show

        raise AssertionError("Unexpected action: {0}".format(name))

    monkeypatch.setattr(service.tk, "get_action", fake_get_action)
    monkeypatch.setattr(service.model, "Session", FakeSession())

    report = build_quality_report({})

    assert report["total_datasets"] == 2
    assert report["average_quality_score"] == 60.0
    assert [dataset["title"] for dataset in report["lowest_quality_datasets"]] == [
        "Dataset B",
        "Dataset A",
    ]
