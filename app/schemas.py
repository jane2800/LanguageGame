from pydantic import BaseModel

#LanguageSchema
class LanguageBase(BaseModel):
    name : str

class LanguageCreate(LanguageBase):
    pass 

class LanguageRead(LanguageBase):
    id : int

    class Config:
        orm_mode = True

#Cities Schema
class CitiesBase(BaseModel):
    name : str

class CitiesCreate(CitiesBase):
    pass 

class CitiesRead(CitiesBase):
    id : int

    class Config:
        orm_mode = True

class AccountCreate(BaseModel):
    game_key : int
    system_language : str
    goal_language : str

class AccountRead(BaseModel):
    id : int
    total_score : int
    system_language : LanguageRead
    goal_language : LanguageRead


    class Config:
        orm_mode = True

# users don't create goals, they are pre-set by developer
class GoalsRead(BaseModel):
    city1: CitiesRead
    city2: CitiesRead
    score: int

    class Config:
        orm_mode = True
    
class GameGoalsRead(BaseModel): 
    id : int
    game_id : AccountRead