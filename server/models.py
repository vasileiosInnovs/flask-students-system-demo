from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, MetaData

metata = MetaData()

db = SQLAlchemy(metadata=metata)

class Student(db.Model):
    
    __tablename__ = "students"
    id = Column(Integer(), primary_key=True)
    name = Column(String(80), nullable=False)
    age = Column(Integer())

class Course(db.Model):
    __tablename__ = "courses"

    id = Column(Integer(), primary_key=True)
    name = Column(String())


class Gender(db.Model):
    __tablename__ = "gender"

    id = Column(Integer(), primary_key=True)
    name = Column(String())