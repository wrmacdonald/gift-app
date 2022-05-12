import pytest
import os
from config import Config

Config.MODE = 'TEST'

from database.database import init_db


@pytest.fixture(scope='session')
def test_db():
    """
    creates a test in-memory db
    yields to tests
    then deletes the database
    """
    init_db()

    yield

    _db = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'test.db')
    if os.path.exists(_db):
        os.remove(_db)
