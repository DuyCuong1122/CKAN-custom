# encoding: utf-8

import pytest

import ckan.tests.factories as factories
import ckan.tests.helpers as helpers


pytestmark = [
    pytest.mark.usefixtures("clean_db", "clean_index"),
]


def _create_dataset(
    sysadmin,
    name,
    title,
    notes="",
    tags=None,
    resources=None,
    owner_org=None,
    license_id="",
    private=False,
):
    return helpers.call_action(
        "package_create",
        context={"user": sysadmin["name"]},
        name=name,
        title=title,
        notes=notes,
        tags=tags or [],
        resources=resources or [],
        owner_org=owner_org,
        license_id=license_id,
        private=private,
    )


@pytest.fixture
def sysadmin():
    return factories.SysadminWithToken()


@pytest.fixture
def user():
    return factories.UserWithToken()


@pytest.fixture
def organization(sysadmin):
    return helpers.call_action(
        "organization_create",
        context={"user": sysadmin["name"]},
        name="quality-org",
        title="Quality Org",
    )


def test_dataset_detail_page_renders_quality_score(app, sysadmin, organization):
    dataset = _create_dataset(
        sysadmin,
        name="quality-detail",
        title="Quality Detail",
        notes="x" * 120,
        tags=[{"name": "quality"}],
        resources=[{"url": "https://example.com/data.csv", "format": "CSV"}],
        owner_org=organization["id"],
        license_id="cc-by",
    )

    response = app.get(f"/dataset/{dataset['name']}")

    assert "Quality Score" in response.text
    assert "100/100" in response.text


def test_dataset_search_page_renders_quality_score(app, sysadmin, organization):
    _create_dataset(
        sysadmin,
        name="quality-search",
        title="Quality Search",
        notes="x" * 120,
        tags=[{"name": "quality"}],
        resources=[{"url": "https://example.com/data.csv", "format": "CSV"}],
        owner_org=organization["id"],
        license_id="cc-by",
    )

    response = app.get("/dataset/")

    assert "Quality Search" in response.text
    assert "Quality Score" in response.text
    assert "100/100" in response.text


def test_dataset_search_page_renders_quality_report_button(app):
    response = app.get("/dataset/")

    assert "Quality Report" in response.text
    assert "/dataset/quality-report" in response.text


def test_organization_page_renders_quality_score(app, sysadmin, organization):
    _create_dataset(
        sysadmin,
        name="quality-org-dataset",
        title="Quality Org Dataset",
        notes="x" * 120,
        tags=[{"name": "quality"}],
        resources=[{"url": "https://example.com/data.csv", "format": "CSV"}],
        owner_org=organization["id"],
        license_id="cc-by",
    )

    response = app.get(f"/organization/{organization['name']}")

    assert "Quality Org Dataset" in response.text
    assert "Quality Score" in response.text


def test_quality_filters_work_on_search_pages(app, sysadmin, organization):
    _create_dataset(
        sysadmin,
        name="quality-high",
        title="Quality High",
        notes="x" * 120,
        tags=[{"name": "quality"}],
        resources=[{"url": "https://example.com/data.csv", "format": "CSV"}],
        owner_org=organization["id"],
        license_id="cc-by",
    )
    _create_dataset(
        sysadmin,
        name="quality-medium",
        title="Quality Medium",
        notes="x" * 120,
        tags=[{"name": "quality"}],
    )
    _create_dataset(
        sysadmin,
        name="quality-low",
        title="Quality Low",
    )

    high = app.get("/dataset/?ext_quality=high")
    medium = app.get("/dataset/?ext_quality=medium")
    low = app.get("/dataset/?ext_quality=low")

    assert "Quality High" in high.text
    assert "Quality Medium" not in high.text
    assert "Quality Low" not in high.text

    assert "Quality High" in medium.text
    assert "Quality Medium" in medium.text
    assert "Quality Low" not in medium.text

    assert "Quality Low" in low.text
    assert "Quality High" not in low.text
    assert "Quality Medium" not in low.text


def test_quality_filters_ignore_duplicate_query_params(app, sysadmin, organization):
    _create_dataset(
        sysadmin,
        name="quality-duplicate-medium",
        title="Quality Duplicate Medium",
        notes="x" * 120,
        tags=[{"name": "quality"}],
    )
    _create_dataset(
        sysadmin,
        name="quality-duplicate-low",
        title="Quality Duplicate Low",
    )

    response = app.get("/dataset/?ext_quality=medium&ext_quality=low")

    assert response.status_code == 200
    assert "Quality Duplicate Low" in response.text
    assert "Quality Duplicate Medium" not in response.text


def test_quality_report_page_renders_summary_and_lowest_datasets(
    app, sysadmin, organization
):
    _create_dataset(
        sysadmin,
        name="quality-report-high",
        title="Quality Report High",
        notes="x" * 120,
        tags=[{"name": "quality"}],
        resources=[{"url": "https://example.com/data.csv", "format": "CSV"}],
        owner_org=organization["id"],
        license_id="cc-by",
    )
    _create_dataset(
        sysadmin,
        name="quality-report-medium",
        title="Quality Report Medium",
        notes="x" * 120,
        tags=[{"name": "quality"}],
    )
    _create_dataset(
        sysadmin,
        name="quality-report-low",
        title="Quality Report Low",
    )

    response = app.get("/dataset/quality-report")

    assert "Dataset Quality Report" in response.text
    assert "Total Datasets" in response.text
    assert "3" in response.text
    assert "Average Score" in response.text
    assert "58.3" in response.text
    assert "Quality Report Low" in response.text


def test_quality_report_page_counts_private_datasets_visible_to_sysadmin(
    app, sysadmin, organization
):
    _create_dataset(
        sysadmin,
        name="quality-report-public",
        title="Quality Report Public",
        owner_org=organization["id"],
    )
    _create_dataset(
        sysadmin,
        name="quality-report-private",
        title="Quality Report Private",
        owner_org=organization["id"],
        private=True,
    )

    response = app.get("/dataset/quality-report", extra_environ={"REMOTE_USER": sysadmin["name"]})

    assert "Total Datasets" in response.text
    assert "2" in response.text
    assert "Quality Report Private" in response.text


def test_quality_report_api_requires_authentication(app):
    response = app.get("/api/3/action/quality_report", status=401)

    assert response.json["success"] is False
    assert response.json["error"]["message"] == "Authentication required"


def test_quality_report_api_returns_summary_for_authenticated_users(
    app, sysadmin, user, organization
):
    _create_dataset(
        sysadmin,
        name="quality-api-high",
        title="Quality API High",
        notes="x" * 120,
        tags=[{"name": "quality"}],
        resources=[{"url": "https://example.com/data.csv", "format": "CSV"}],
        owner_org=organization["id"],
        license_id="cc-by",
    )
    _create_dataset(
        sysadmin,
        name="quality-api-low",
        title="Quality API Low",
    )

    response = app.get(
        "/api/3/action/quality_report",
        headers={"Authorization": user["token"]},
    )

    assert response.status_code == 200
    assert response.json["success"] is True
    assert response.json["result"] == {
        "total_datasets": 2,
        "average_quality_score": 60.0,
    }
