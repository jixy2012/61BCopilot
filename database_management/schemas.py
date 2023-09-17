'''
Pydantic Models
'''

from typing import Optional
from pydantic import BaseModel, Field
from typing import List, Optional
from pydantic import BaseModel

class ProblemBase(BaseModel):
    number: int
    semester: str
    difficulty: str
    professor: str
    text: str

class ProblemCreate(ProblemBase):
    number: int
    semester: str
    difficulty: str
    professor: str
    text: str
    topics: Optional[List[str]] = []

class Problem(ProblemBase):
    id: int
    topics: List[str]  # Assuming you want to just send topic names as a list

    class Config:
        orm_mode = True

class TopicBase(BaseModel):
    topic: str

class TopicCreate(TopicBase):
    topic: str

class Topic(TopicBase):
    id: int
    problems: List[Problem]

    class Config:
        orm_mode = True
