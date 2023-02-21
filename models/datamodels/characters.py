"""pydantic model for characters data coming from swapi.dev/api/people"""

from pydantic import BaseModel
from models.basemodel import Base
from typing import List, Optional


class Character_(BaseModel):
class Character_(Base):
    name: str
    height: str
    mass: str
class Character_(BaseModel):

    obj = Character_(**external)
    print(obj)
    breakpoint()
