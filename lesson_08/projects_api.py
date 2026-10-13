import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class ProjectsApi:
    """Работа с проектами через YouGile REST API v2."""

    TIMEOUT = 30

    def __init__(self, base_url, api_key=None):
        self.url = base_url.rstrip("/") + "/api-v2/projects"
        # Одна сессия на все запросы: соединение с сервером
        # переиспользуется, а заголовки задаются один раз
        self.session = requests.Session()
        self.session.headers["Content-Type"] = "application/json"
        if api_key:
            self.session.headers["Authorization"] = f"Bearer {api_key}"
        # Повтор только при сетевом сбое, когда ответа от сервера нет.
        # POST после обрыва не повторяется, чтобы не создать дубль проекта
        retry = Retry(total=3, connect=3, read=3, status=0,
                      backoff_factor=1)
        self.session.mount("https://", HTTPAdapter(max_retries=retry))

    # [POST] /api-v2/projects — создать проект
    def create_project(self, body):
        return self.session.post(self.url, json=body, timeout=self.TIMEOUT)

    # [PUT] /api-v2/projects/{id} — изменить проект
    def update_project(self, project_id, body):
        return self.session.put(f"{self.url}/{project_id}", json=body,
                                timeout=self.TIMEOUT)

    # [GET] /api-v2/projects/{id} — получить проект по id
    def get_project(self, project_id):
        return self.session.get(f"{self.url}/{project_id}",
                                timeout=self.TIMEOUT)

    # Метода DELETE для проектов в API нет:
    # проект удаляется изменением с полем deleted = true
    def delete_project(self, project_id):
        return self.update_project(project_id, {"deleted": True})
