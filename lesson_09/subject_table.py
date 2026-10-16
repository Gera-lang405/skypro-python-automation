from sqlalchemy import create_engine, text

# Драйвер по заданию — psycopg2-binary. SQLAlchemy 2.1 для схемы
# postgresql:// по умолчанию ищет другой драйвер (psycopg 3),
# поэтому драйвер указывается явно
DRIVER_PREFIXES = ("postgresql://", "postgres://")


def with_psycopg2(connection_string):
    for prefix in DRIVER_PREFIXES:
        if connection_string.startswith(prefix):
            return "postgresql+psycopg2://" + connection_string[len(prefix):]
    return connection_string


class SubjectTable:
    """Работа с таблицей subject (предметы) через SQLAlchemy."""

    def __init__(self, connection_string):
        self.db = create_engine(with_psycopg2(connection_string))

    def get_max_id(self):
        sql = text("SELECT MAX(subject_id) FROM subject")
        with self.db.connect() as connection:
            return connection.execute(sql).scalar() or 0

    def get_by_id(self, subject_id):
        sql = text("SELECT subject_id, subject_title FROM subject "
                   "WHERE subject_id = :id")
        with self.db.connect() as connection:
            result = connection.execute(sql, {"id": subject_id})
            row = result.mappings().first()
        return dict(row) if row else None

    def create(self, subject_id, title):
        sql = text("INSERT INTO subject (subject_id, subject_title) "
                   "VALUES (:id, :title)")
        # begin() сам делает commit после выполнения запроса
        with self.db.begin() as connection:
            connection.execute(sql, {"id": subject_id, "title": title})

    def update_title(self, subject_id, title):
        sql = text("UPDATE subject SET subject_title = :title "
                   "WHERE subject_id = :id")
        with self.db.begin() as connection:
            connection.execute(sql, {"id": subject_id, "title": title})

    def delete(self, subject_id):
        sql = text("DELETE FROM subject WHERE subject_id = :id")
        with self.db.begin() as connection:
            connection.execute(sql, {"id": subject_id})
