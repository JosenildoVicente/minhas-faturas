# import pandas as pd
from create_database import create_db, populate_db, view_tables

if __name__ == "__main__":
    create_db()
    populate_db()
    view_tables()