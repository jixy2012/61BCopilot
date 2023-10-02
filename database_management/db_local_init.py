from .database import engine
from . import models
from .models import Base


def init_db():
    try:
        conn = engine.connect()
        conn.close()
        print('successful connection')
    except:
        print('fuck')
    Base.metadata.create_all(bind=engine)

