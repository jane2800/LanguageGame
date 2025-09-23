from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from pydantic import BaseModel
from typing import List, Annotated

from app.api.setup import router as random_router

app = FastAPI() 

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="app/templates")

app.include_router(random_router)

from fastapi import Request
from fastapi.responses import HTMLResponse

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/game", response_class=HTMLResponse)
async def game_page(request: Request):
    return templates.TemplateResponse("game.html", {"request": request})

@app.get("/continue-game", response_class=HTMLResponse)
async def continueGame_page(request: Request):
    return templates.TemplateResponse("continue-game.html", {"request": request})

@app.get("/new-game", response_class=HTMLResponse)
async def newGame_page(request: Request):
    return templates.TemplateResponse("new-game.html", {"request": request})

@app.get("/quiz", response_class=HTMLResponse)
async def quiz_page(request: Request):
    return templates.TemplateResponse("quiz.html", {"request": request})

@app.get("/quiz-q", response_class=HTMLResponse)
async def quiz_question_page(request: Request):
    return templates.TemplateResponse("quiz-q.html", {"request":request})
