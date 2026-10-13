# Урок 8. API-тесты YouGile: проекты

Тесты на методы:

- `[POST] /api-v2/projects` — создание проекта;
- `[PUT] /api-v2/projects/{id}` — изменение проекта;
- `[GET] /api-v2/projects/{id}` — получение проекта по id.

## Что нужно для запуска

Ключ API YouGile в переменной окружения `YOUGILE_API_KEY`.
В коде ключа нет.

Ключ можно получить запросом `POST https://ru.yougile.com/api-v2/auth/keys`
с телом `{"login": "...", "password": "...", "companyId": "..."}`
(id компании возвращает `POST /api-v2/auth/companies`).

Windows (PowerShell):

```powershell
$env:YOUGILE_API_KEY = "ваш_ключ"
pytest lesson_08
```

Windows (cmd):

```bat
set YOUGILE_API_KEY=ваш_ключ
pytest lesson_08
```

macOS / Linux:

```bash
export YOUGILE_API_KEY="ваш_ключ"
pytest lesson_08
```

Необязательно: `YOUGILE_URL` — адрес сервера, по умолчанию
`https://ru.yougile.com`.

Тесты сами создают нужные проекты и после себя удаляют их
(в API нет метода DELETE, поэтому проекту ставится `deleted: true`).
