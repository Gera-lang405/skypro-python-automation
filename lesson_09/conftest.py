import os
import uuid

import pytest

from subject_table import SubjectTable


@pytest.fixture(scope="session")
def subject_table():
    """Таблица subject; строка подключения берётся из окружения."""
    connection_string = os.getenv("DB_CONNECTION_STRING")
    if not connection_string:
        pytest.fail("Не задана строка подключения к БД: укажите её "
                    "в переменной окружения DB_CONNECTION_STRING")
    table = SubjectTable(connection_string)
    yield table
    table.db.dispose()


@pytest.fixture
def unique_title():
    """Уникальное название, чтобы повторные запуски не мешали друг другу."""
    return f"Autotest {uuid.uuid4().hex[:8]}"


@pytest.fixture
def created_ids(subject_table):
    """id предметов, созданных в тесте; после теста они удаляются из БД."""
    ids = []
    yield ids
    for subject_id in ids:
        subject_table.delete(subject_id)


@pytest.fixture
def new_subject(subject_table, created_ids):
    """Предмет, созданный для теста изменения или удаления."""
    subject_id = subject_table.get_max_id() + 1
    title = f"Autotest subject {uuid.uuid4().hex[:8]}"
    subject_table.create(subject_id, title)
    created_ids.append(subject_id)
    return {"subject_id": subject_id, "subject_title": title}
