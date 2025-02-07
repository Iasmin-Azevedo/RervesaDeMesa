from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from services.mesas_service import (
    fetch_mesas,
    add_mesas,
    delete_mesas_service,
    fetch_mesas_by_id,
    update_mesas_service,
)

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/mesas")
def listar_mesas(request: Request):
    mesas = fetch_mesas()
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "titulo": "Lista de mesas",
            "colunas": ["ID", "Área", "Capacidade"],
            "itens": mesas,
            "url_add": "/mesas/novo",
            "url_editar": "/mesas/editar",
            "url_excluir": "/mesas/excluir",
        },
    )


@router.get("/mesas/novo")
def form_nova_mesas(request: Request):
    return templates.TemplateResponse(
        "form.html",
        {
            "request": request,
            "titulo": "Nova mesas",
            "url_salvar": "/mesas/salvar",
            "url_voltar": "/mesas",
            "campos": {"id": "","nome": "", "capacidade": ""},
        },
    )

@router.post("/mesas/salvar")
def salvar_mesas(
    id: str = Form(...),
    nome: str = Form(...),
    capacidade: int = Form(...),
):
    nova_mesas = {
        "id": id,
        "nome": nome,
        "capacidade": capacidade,
    }
    return add_mesas(nova_mesas)


@router.get("/mesas/editar/{mesas_id}")
def form_editar_mesas(request: Request, mesas_id: int):
    mesas = fetch_mesas_by_id(mesas_id)
    if not mesas:
        raise HTTPException(status_code=404, detail="mesas não encontrada")

    return templates.TemplateResponse(
        "form.html",
        {
            "request": request,
            "titulo": "Editar mesas",
            "url_salvar": f"/mesas/atualizar/{mesas_id}",
            "url_voltar": "/mesas",
            "campos": mesas,
        },
    )


@router.post("/mesas/atualizar/{mesas_id}")
def atualizar_mesas(
    mesas_id: int,
    nome: str = Form(...),
    capacidade: int = Form(...),
):
    if not nome or not capacidade:
        raise HTTPException(
            status_code=400, detail="Nome e Capacidade são obrigatórios"
        )

    updated_data = {
        "nome": nome,
        "capacidade": capacidade,
    }
    updated_mesas = update_mesas_service(mesas_id, updated_data)
    if not updated_mesas:
        raise HTTPException(status_code=404, detail="mesas não encontrada")

    return updated_mesas


@router.get("/mesas/excluir/{mesas_id}")
def excluir_mesas(mesas_id: int):
    if delete_mesas_service(mesas_id):
        return {"message": "mesas deletada com sucesso"}
    raise HTTPException(status_code=404, detail="mesas não encontrada")
