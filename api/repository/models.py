import sqlalchemy as sa
from repository.db import base, conection

class Student(base):
    __tablename__ = "estudiante"
    id = sa.Column(sa.Integer, autoincrement=True, primary_key=True)
    username = sa.Column(sa.String(200))
    nombre = sa.Column(sa.String(200))
    edad = sa.Column(sa.Integer)
    pregrado = sa.Column(sa.String(100))
    semestre_actual = sa.Column(sa.Integer)
    tranporte = sa.Column(sa.String(100))


""" class Carrera(base):
    pass

class parking(base):
    pass 
class Tranporte(base): #Puede ser un tributo de studiante
    pass
class Biblioteca(base):
    pass """
    

base.metadata.create_all(conection)
