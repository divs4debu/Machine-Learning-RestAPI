from sqlalchemy import Column, String, Integer, DateTime, ForeignKey,ARRAY
from Base import Base

class Request(Base):

    __tablename__ = 'REQUESTS'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('USERS.id'))
    type = Column(String(255), nullable=False)
    receive_time = Column(DateTime)
    deliver_time = Column(DateTime)
