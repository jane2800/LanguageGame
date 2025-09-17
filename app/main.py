from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.api.setup import router as random_router

app = FastAPI()

# Serve static files (CSS/JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates (HTML pages)
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

@app.get("/continueGame", response_class=HTMLResponse)
async def continueGame_page(request: Request):
    return templates.TemplateResponse("continueGame.html", {"request": request})

@app.get("/newGame", response_class=HTMLResponse)
async def newGame_page(request: Request):
    return templates.TemplateResponse("newGame.html", {"request": request})