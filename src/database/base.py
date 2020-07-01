import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('{}://{}:{}@{}:{}/{}'.format(os.getenv('DIALECT'), os.getenv("UID"), os.getenv("PASSWORD"),
                                                    os.getenv("HOSTNAME"),
                                                    os.getenv("DB2_PORT"), os.getenv("DATABASE")), echo=True)
# use session_factory() to get a new Session
_SessionFactory = sessionmaker(bind=engine)

Base = declarative_base()


def session_factory(base):
    if base is not None and not engine.dialect.has_table(connection=engine, table_name=base.__table__.fullname,
                                                         schema=os.getenv("SCHEMA_NAME")):
        base.metadata.create_all(engine)
    return _SessionFactory()
