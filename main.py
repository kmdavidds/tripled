from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware 
from util import getVideos
import uvicorn 

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
) 

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )

@app.get("/signup", response_class=HTMLResponse)
async def signup(request: Request):
    return templates.TemplateResponse(
        request=request, name="signup.html"
    )

@app.get("/datasiswa", response_class=HTMLResponse)
async def datasiswa(request: Request):
    return templates.TemplateResponse(
        request=request, name="datasiswa.html"
    )

@app.get("/homepage", response_class=HTMLResponse)
async def homepage(request: Request):
    videos = getVideos()
    return templates.TemplateResponse(
        request=request, name="homepage.html", context={"videopath": "", "videos": videos}
    )

@app.get("/homepage/{videopath}", response_class=HTMLResponse)
async def homepage(request: Request, videopath: str):
    videos = getVideos()
    return templates.TemplateResponse(
        request=request, name="homepage.html", context={"videopath": f"videos/{videopath}", "videos": videos}
    )

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)