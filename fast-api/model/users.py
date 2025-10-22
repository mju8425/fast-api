from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta_data, engine


users = Table(
    "users",
    meta_data,
    Column("id", Integer, primary_key=True),
    Column("name", String(200), nullable=False),
    Column("email", String(200), nullable=False),
    Column("password", String(200), nullable=False))

meta_data.create_all(engine)
