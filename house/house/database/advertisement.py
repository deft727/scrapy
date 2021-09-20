from sqlalchemy import Column, Integer, String
from .mydb import Base


class Advertisement(Base):
    __tablename__ = 'advertisement'

    id = Column(Integer, primary_key=True)
    # link = Column(String)
    title = Column(String)
    # address = Column(String)
    # description = Column(String)
    # space = Column(String)
    # image = Column(String)
    # saller = Column(String)

    def __repr__(self):
        return f'advertisement [ID: {self.id}, TITLE: {self.title}]'