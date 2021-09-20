
import os
from .mydb import DATABASE_NAME
from . import create_db as db_creator


if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()