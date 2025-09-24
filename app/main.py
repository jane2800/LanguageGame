from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from typing import List, Annotated
from sqlalchemy.orm import Session
from app.database import get_db, Base, engine
from . import crud, models
from . import schemas

Base.metadata.create_all(bind=engine)

from app.api.setup import router as random_router

app = FastAPI() 

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="app/templates")

app.include_router(random_router)

from fastapi import Request
from fastapi.responses import HTMLResponse

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(
        "index.html", 
        {"request": request})

@app.get("/game", response_class=HTMLResponse)
async def game_page(request: Request):
    return templates.TemplateResponse("game.html", {"request": request})

@app.get("/continue-game", response_class=HTMLResponse)
async def continueGame_page(request: Request):
    return templates.TemplateResponse("continue-game.html", {"request": request})

#crud.create_account
@app.get("/new-game", response_class=HTMLResponse)
async def newGame_page(request: Request):
    return templates.TemplateResponse("new-game.html", {"request": request, 
                                                        "gamekey": None})

@app.post("/generate-key", response_class=HTMLResponse)
async def generate_key(request: Request, session : Session = Depends(get_db)):
        account_data = schemas.AccountCreate(system_language="EN", goal_language="DE")
        account = crud.create_account(session, account_data)
        return templates.TemplateResponse(
        "new-game.html",
        {"request": request, "gamekey": account.game_key, "account": account}
        )

@app.get("/quiz", response_class=HTMLResponse)
async def quiz_page(request: Request):
    return templates.TemplateResponse("quiz.html", {"request": request})

@app.get("/quiz-q", response_class=HTMLResponse)
async def quiz_question_page(request: Request):
    return templates.TemplateResponse("quiz-q.html", {"request":request})
