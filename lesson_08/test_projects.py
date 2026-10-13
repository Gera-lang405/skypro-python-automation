import uuid

UNAUTHORIZED = "Unauthorized"
PROJECT_NOT_FOUND = "Проект не найден"


def not_existing_id():
    return str(uuid.uuid4())


# ---------- [POST] /api-v2/projects ----------

def test_create_project(api, created_ids, title):
    resp = api.create_project({"title": title})

    assert resp.status_code == 201
    project_id = resp.json()["id"]
    created_ids.append(project_id)
    assert project_id

    project = api.get_project(project_id).json()
    assert project["id"] == project_id
    assert project["title"] == title


def test_create_project_without_title(api):
    resp = api.create_project({})

    assert resp.status_code == 400
    assert "title should not be empty" in resp.json()["message"]


def test_create_project_without_auth(api_without_auth, title):
    resp = api_without_auth.create_project({"title": title})

    assert resp.status_code == 401
    assert resp.json()["message"] == UNAUTHORIZED


# ---------- [PUT] /api-v2/projects/{id} ----------

def test_update_project_title(api, project, title):
    resp = api.update_project(project["id"], {"title": title})

    assert resp.status_code == 200
    assert resp.json()["id"] == project["id"]

    updated = api.get_project(project["id"]).json()
    assert updated["title"] == title


def test_update_project_with_wrong_title_type(api, project):
    resp = api.update_project(project["id"], {"title": 12345})

    assert resp.status_code == 400
    assert "title must be a string" in resp.json()["message"]


def test_update_not_existing_project(api, title):
    resp = api.update_project(not_existing_id(), {"title": title})

    assert resp.status_code == 404
    assert resp.json()["message"] == PROJECT_NOT_FOUND


# ---------- [GET] /api-v2/projects/{id} ----------

def test_get_project_by_id(api, project):
    resp = api.get_project(project["id"])

    assert resp.status_code == 200
    body = resp.json()
    assert body["id"] == project["id"]
    assert body["title"] == project["title"]
    assert body.get("deleted", False) is False


def test_get_not_existing_project(api):
    resp = api.get_project(not_existing_id())

    assert resp.status_code == 404
    assert resp.json()["message"] == PROJECT_NOT_FOUND


def test_get_project_without_auth(api_without_auth, project):
    resp = api_without_auth.get_project(project["id"])

    assert resp.status_code == 401
    assert resp.json()["message"] == UNAUTHORIZED
