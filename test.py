from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

raciones = [
    {"nombre":"Oreja","descripcion":"Crujiente oreja a la plancha","url":"racion1.png"},
    {"nombre":"Bravas","descripcion":"Patatas con un toque chili","url":"racion2.png"},
    {"nombre":"Calamares","descripcion":"Recien traidos del mar","url":"racion3.png"},
] 
#bucle que dibuja tabla


@app.get("/carpe", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,                
        name="carpe.html", 
        context={})



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("test:app", reload=True)