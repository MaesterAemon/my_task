"""
Подключение бд
"""
import sqlalchemy

from databases import Database

DATABASE_URL = 'postgresql://postgres:password@localhost/postgres'

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata = sqlalchemy.MetaData()

table = sqlalchemy.Table(
    'my_table',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('datetime', sqlalchemy.DateTime),
    sqlalchemy.Column('address', sqlalchemy.String(50)))

database = Database(DATABASE_URL)
