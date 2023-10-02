
from database_management.db_local_init import init_db
from database_management.models import *
from database_management.schemas import *
from database_management.crud import *
from database_management.database import *
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def test_add_one_topic():
    db_session = SessionLocal()
    try:
        init_db()
        topic_inheritance = TopicCreate(topic='inheritance')
        added_topic = add_topic(db=db_session, topic_to_add=topic_inheritance)
        # Fetch the topic from the database
        fetched_topic = db_session.query(ExamTopic).filter_by(topic='inheritance').first()
        assert fetched_topic is not None, "Topic was not added to the database"
        logging.debug("finished adding one topic!")
    except Exception as e:
        print('somthing went wrong!')
        logging.error(f"Exception: {e}")
    finally:
        db_session.close()
        logging.debug('closed session')

