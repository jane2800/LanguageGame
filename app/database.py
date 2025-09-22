from sqlalchemy import create_engine;
from sqlalchemy.orm import sessionmaker;
from sqlalchemy.ext.declarative import declarative_base;

URL_DATABASE = 'postgresql://postgres:corn1234@localhost:5432/LanguageGame'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocomit=False, autoflush=False, bind=engine)

Base = declarative_base