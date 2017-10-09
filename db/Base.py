from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

db_engine = create_engine('mysql://root:3n19m4@localhost/ml_api', echo=True)

Base = declarative_base(db_engine)