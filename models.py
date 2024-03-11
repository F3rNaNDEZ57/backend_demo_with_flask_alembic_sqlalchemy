from sqlalchemy import INTEGER, Column, String
from database import Session, engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = "user"

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)


