import sqlalchemy as sa
from repository.db import base, conection

class Student(base):
    __tablename__ = "estudiante"
    id = sa.Column(sa.Integer, autoincrement=True, primary_key=True)
    username = sa.Column(sa.String(200))
    

base.metadata.create_all(conection)
