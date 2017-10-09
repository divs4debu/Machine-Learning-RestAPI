from Base import Base, db_engine

from User import User
from Request import Request

Base.metadata.create_all(db_engine)
