'''
Database Operations
functions: ur standard create read update delete ops
'''
from sqlalchemy.sql import func
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from .models import *
from .schemas import *

def add_topic(db: Session, topic_to_add: TopicCreate) -> ExamTopic:
    db_new_topic = ExamTopic(topic=topic_to_add.topic)
    try:
        db.add(db_new_topic)
        db.commit()
        db.refresh(db_new_topic)
        return db_new_topic
    except IntegrityError:
        db.rollback()
        raise ValueError(f"Duplicate topic value {topic_to_add.topic} cannot be added to topics table.")
    
    

def add_problem(db: Session, problem_to_add: ProblemCreate) -> ExamProblem:

    try:

        db_topics = db.query(ExamTopic).filter(ExamTopic.topic.in_(problem_to_add.topics)).all()

        if len(db_topics) != len(problem_to_add.topics):
            missing_topics = set(problem_to_add.topics) - {topic.topic for topic in db_topics}
            raise ValueError(f"The following topics do not exist in the database: {', '.join(missing_topics)}")

        db_new_problem = ExamProblem(
            number=problem_to_add.number,
            semester=problem_to_add.semester,
            difficulty=problem_to_add.difficulty,
            professor=problem_to_add.professor,
            text=problem_to_add.text,
            topics=db_topics
        )
        db.add(db_new_problem)
        db.commit()
        db.refresh()
        return db_new_problem
    except Exception as e:
        db.rollback()
        return Exception(f"When added a new problem to the database a {e} occurred. Entry creation stopped.")