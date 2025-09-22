from sqlalchemy import Boolean, Column, Integer, ForeignKey, String, DateTime, func 
from database import Base

class Account(Base):
    __tablename__ = 'accounts' 

    id = Column(Integer, primary_key=True, index=True)
    game_key = Column(Integer, unique=True, nullable=False)
    total_score = Column(Integer, default=0)
    system_language = Column(Integer, ForeignKey("languages.id"))
    goal_language = Column(Integer, ForeignKey("languages.id"))

class Language(Base):
    __tablename__ = 'languages'

    id = Column(primary_key=True, index=True)
    name = Column(String, nullable=False)

class Cities(Base):
    __tablename__ = 'cities'

    id = Column(primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)

class Goals(Base):
    __tablename__ = 'goals'

    id = Column(primary_key=True, index=True)
    city1 = Column(Integer, ForeignKey("cities.id"))
    city2 = Column(Integer, ForeignKey("cities.id"))
    score = Column(Integer, nullable=False)

class GameGoals(Base):
    __tablename__ = 'gamegoals'
     
    id = Column(primary_key=True, index=True)
    game_id = Column(Integer, ForeignKey("accounts.id"))
    goal_id = Column(Integer, ForeignKey("goals.id"))
    goal_complete = Column(Boolean)

class Mapping(Base):
    __tablename__ = 'mapping'
     
    id = Column(primary_key=True, index=True)
    city1 = Column(Integer, ForeignKey("cities.id"))
    city2 = Column(Integer, ForeignKey("cities.id"))
    length = Column(Integer, nullable=False)
    color = Column(Integer, ForeignKey("colors.id"))

class Color(Base):
    __tablename__ = 'colors'

    id = Column(primary_key=True, index=True)
    name = Column(String, nullable=False)
    active = Column(String, nullable=False)
    hex = Column(String, nullable=False)

class PlayerPath(Base):
    __tablename__ = 'playerpath'

    id = Column(primary_key=True, index=True)   
    game_id = Column(Integer, ForeignKey("accounts.id"))
    destination_id = Column(Integer, ForeignKey("mapping.id"))
    timestamp = Column(DateTime(timezone=True), server_default=func.now(), index=True)

class UserAnswer(Base):
    __tablename__ = 'useranswer'

    id = Column(primary_key=True, index=True)  
    game_id = Column(Integer, ForeignKey("accounts.id"))
    question_id = Column(Integer, ForeignKey("quizquestion.id"))
    user_and = Column(String, nullable=False)
    is_correct = Column(Boolean, default=False)

class QuizQuestions(Base):
    __tablename__ = 'quizquestions'

    id = Column(primary_key=True, index=True)
    question_text = Column(String, nullable=False)
    question_ans = Column(String, nullable=False)
    quiz_id = Column(Integer, ForeignKey("quiz.id"))

class Quiz(Base):
    __tablename__ = 'quiz'

    id = Column(primary_key=True, index=True)
    title = Column(String, nullable=False)
    level = Column(String, nullable=False)
    is_complete = Column(Boolean, default=False)



