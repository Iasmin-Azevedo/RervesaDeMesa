from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from controllers.mesas_controller import router as quadra_router
from controllers.reservas_controller import router as agendamento_router

app = FastAPI()

# Configuração dos arquivos estáticos
app.mount("/static", StaticFiles(directory="./templates/static"), name="static")

# Configuração do Jinja2 para templates
templates = Jinja2Templates(directory="templates")

# Registrando as rotas
app.include_router(quadra_router, tags=["Quadra"])
app.include_router(agendamento_router, tags=["Agendamento"])


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse(
        "home.html", {"request": request, "title": "Home"}
    )
