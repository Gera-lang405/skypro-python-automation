# Урок 9. Тесты работы с БД через SQLAlchemy

Тесты добавления, изменения и удаления записи в таблице `subject`
(предметы) учебной БД из модуля SQL (`subject_id`, `subject_title`).

- `subject_table.py` — класс `SubjectTable`: все запросы к БД через SQLAlchemy;
- `conftest.py` — фикстуры: подключение, создание тестового предмета
  и удаление после теста;
- `test_subject.py` — тесты.

Каждый тест сам создаёт нужный предмет и после выполнения удаляет его
из БД, поэтому тесты можно запускать в любом порядке и сколько угодно раз.

## Что нужно для запуска

1. Установить библиотеки:

   ```
   pip install -r lesson_09/requirements.txt
   ```

2. Задать строку подключения к своей БД в переменной окружения
   `DB_CONNECTION_STRING` (в коде данных для подключения нет):

   Windows (PowerShell):

   ```powershell
   $env:DB_CONNECTION_STRING = "postgresql://myuser:mypassword@localhost:5432/mydatabase"
   ```

   Windows (cmd):

   ```bat
   set DB_CONNECTION_STRING=postgresql://myuser:mypassword@localhost:5432/mydatabase
   ```

   macOS / Linux:

   ```bash
   export DB_CONNECTION_STRING="postgresql://myuser:mypassword@localhost:5432/mydatabase"
   ```

3. Запустить тесты:

   ```
   pytest lesson_09
   ```
