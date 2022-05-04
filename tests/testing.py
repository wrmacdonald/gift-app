from database.database import drop_db, init_db


def setup_db():
    drop_db()
    init_db()
