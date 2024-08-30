from pydantic import BaseModel
from enum import Enum

class FamilyEnum(str, Enum):
    Tokugawa = "Tokugawa"
    Oda = "Oda"
    Toyotomi = "Toyotomi"
    Takeda = "Takeda"

class Power(BaseModel):
    name: str
    force: int

class SamuraiSchema(BaseModel):
    name: str
    age: int
    family: FamilyEnum
    power: Power

class SamuraiCreateSchema(BaseModel):
    age: int
    family: FamilyEnum
    power: Power

class SamuraiResponseSchema(SamuraiSchema):
    id: int