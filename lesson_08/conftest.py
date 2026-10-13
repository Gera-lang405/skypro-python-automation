import os
import uuid

import pytest

from projects_api import ProjectsApi

BASE_URL = os.getenv("YOUGILE_URL", "https://ru.yougile.com")


@pytest.fixture(scope="session")
def api():
    """Клиент API с ключом из переменной окружения YOUGILE_API_KEY."""
    api_key = os.getenv("YOUGILE_API_KEY")
    if not api_key:
        pytest.fail("Не задан ключ API YouGile: "
                    "укажите его в переменной окружения YOUGILE_API_KEY")
    return ProjectsApi(BASE_URL, api_key)


@pytest.fixture(scope="session")
def api_without_auth():
    """Клиент API без заголовка Authorization."""
    return ProjectsApi(BASE_URL)


@pytest.fixture
def title():
    """Уникальное название, чтобы повторные запуски не мешали друг другу."""
    return f"Autotest {uuid.uuid4().hex[:8]}"


@pytest.fixture
def created_ids(api):
    """Проекты, созданные в тесте; после теста они удаляются."""
    ids = []
    yield ids
    for project_id in ids:
        api.delete_project(project_id)


@pytest.fixture
def project(api, created_ids):
    """Заранее созданный проект для тестов изменения и получения."""
    project_title = f"Autotest project {uuid.uuid4().hex[:8]}"
    resp = api.create_project({"title": project_title})
    if resp.status_code != 201:
        pytest.fail(f"Не удалось создать проект: {resp.status_code} "
                    f"{resp.text}")
    project_id = resp.json()["id"]
    created_ids.append(project_id)
    return {"id": project_id, "title": project_title}
