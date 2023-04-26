import sqlalchemy as sa
from repository.db import base, conection

class User(base):
    __tablename__ = "usuario"
    id = sa.Column(sa.Integer, autoincrement=True, primary_key=True)
    email = sa.Column(sa.String(256), unique=True)
    password = sa.Column(sa.String(70))
    username = sa.Column(sa.String(100), unique=True)
    

base.metadata.create_all(conection)
