from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin

metata = MetaData()

db = SQLAlchemy(metadata=metata)

class Student(db.Model, SerializerMixin):
    
    __tablename__ = "students"
    id = Column(Integer(), primary_key=True)
    name = Column(String(80), nullable=False)
    age = Column(Integer())

    enrollments = relationship("Enrollment", back_populates="student")
    serialize_rules = ("-enrollments.student",)

class Course(db.Model, SerializerMixin):
    __tablename__ = "courses"

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    enrollments = relationship("Enrollment", back_populates="course")
    serialize_rules = ("-enrollments.course",)


class Grade(db.Model, SerializerMixin):
    __tablename__ = "grades"

    id = Column(Integer(), primary_key=True)
    name = Column(String())

class Enrollment(db.Model, SerializerMixin):
    __tablename__ = "enrollments"
             
    id = Column(Integer(), primary_key=True)
    student_id = Column(Integer(), ForeignKey("students.id", ondelete="CASCADE"))
    course_id = Column(Integer(), ForeignKey("courses.id", ondelete="CASCADE"))
    grade = Column(String())

    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")

    serialize_rules = ("-student.enrollments", "-course.enrollments",)