from sqlalchemy import Column, String, Integer
from Base import Base


class User(Base):

    __tablename__ = 'USERS'

    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False, unique=True)
    name = Column(String(255), nullable=False)
    phone = Column(Integer)
    password = Column(String(255), nullable=False)
    category = Column(Integer, nullable=False, default=0)

