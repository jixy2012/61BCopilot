'''
SQLAlchemy Models
'''

from sqlalchemy import Table, Boolean, Column, ForeignKey, Integer, String, DateTime, CheckConstraint, Text
from sqlalchemy.orm import relationship
from sqlalchemy import CheckConstraint, column

from .database import Base


problems_topics = Table(
    'problems_topics',
    Base.metadata, 
    Column('problem_id', Integer, ForeignKey('exam_problems.id'), primary_key=True),
    Column('topic_id', Integer, ForeignKey('exam_topics.id'), primary_key=True)
)

class ExamProblem(Base):
    __tablename__ = 'exam_problems'

    id = Column(Integer, primary_key=True, index=True) # unique id of a problem
    semester = Column(String(32), index=True) # semester
    difficulty = Column(String(32))
    professor = Column(Text) # the professor teaching the course. only one professor supported
    text = Column(Text, nullable=False) # main body of the question. preferrably LaTeX format
    topics = relationship('ExamTopic', secondary=problems_topics, back_populates='problems')

    __table_args__ = (
        CheckConstraint(semester.in_([
            'fa23',
            'sp23',
            'fa22',
            'sp22',
        ])),
        CheckConstraint(difficulty.in_([
            'easy', 
            'medium', 
            'hard', 
            'insane'
        ])),
    )

class ExamTopic(Base):
    __tablename__ = 'exam_topics'
    id = Column(Integer, primary_key=True, index=True)
    topic = Column(String, unique=True, nullable=False)
    problems = relationship('ExamProblem', secondary=problems_topics, back_populates='topics')