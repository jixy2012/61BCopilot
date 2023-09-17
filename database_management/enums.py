from sqlalchemy import Enum

class Semester(Enum):
    FA23 = 'fa23'
    SP23 = 'sp23'
    FA22 = 'fa22'
    SP22 = 'sp22'

class Difficulty(Enum):
    EASY = 'easy'
    MEDIUM = 'medium'
    HARD = 'hard'
    INSANE = 'insane'