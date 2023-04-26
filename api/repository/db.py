from sqlalchemy import create_engine #Traducciones para SQL, querys
from sqlalchemy.ext.declarative import declarative_base #Clase que hereda todos los modelos, la que hace el maping de los ORM
from sqlalchemy.orm import sessionmaker #Permite hacer transacciones a la base de datos

DB_USER = "eiapi_user"
DB_PASSWORD = "ifygL63QmrwqHuYhV0Xj1Qzclfu31EqX"
DB_HOST = "dpg-ch41mcr3cv21aod5h02g-a.oregon-postgres.render.com"
DB_PORT = "5432"
DB_NAME = "eiapi"

base = declarative_base()

conection = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}')


session = sessionmaker(bind=conection)
