from sqlalchemy.orm import Session
from . import models, schemas

# app/crud.py
from sqlalchemy.orm import Session
from . import models, schemas
import random

def create_language(db: Session, language: schemas.LanguageCreate):
    db_lang = models.Language(name=language.name)
    db.add(db_lang)
    db.commit()
    db.refresh(db_lang)
    return db_lang

def get_languages(db: Session):
    return db.query(models.Language).all()

def create_account(db: Session, account: schemas.AccountCreate):
    new_game_key = random.randint(1000, 9999)  # Auto-generate game key
    db_account = models.Account(
        game_key=new_game_key,
        total_score=0,
        system_language=account.system_language,
        goal_language=account.goal_language
    )
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account

def get_accounts(db: Session):
    return db.query(models.Account).all()

def get_account(db: Session, game_key : int):
    return db.query(models.Account).filter(models.Account.game_key == game_key).first()
