from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from services.reservas_service import (
    fetch_reservas,
    add_reservas,
    delete_reservas_service,
    fetch_reservas_by_id,
    update_reservas_service,
)

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/reservas")
def listar_reservas(request: Request):
    reservas = fetch_reservas()
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "titulo": "Lista de reservas",
            "colunas": ["ID", "Mesa ID", "Data", "Hora", "Responsável"],
            "itens": reservas,
            "url_add": "/reservas/novo",
            "url_editar": "/reservas/editar",
            "url_excluir": "/reservas/excluir",
        },
    )


@router.get("/reservas/novo")
def form_novo_reservas(request: Request):
    return templates.TemplateResponse(
        "form.html",
        {
            "request": request,
            "titulo": "Novo reservas",
            "url_salvar": "/reservas/salvar",
            "url_voltar": "/reservas",
            "campos": {"mesa_id": "", "data": "", "hora": "", "cliente": ""},
        },
    )


@router.post("/reservas/salvar")
def salvar_reservas(
    mesa_id: int = Form(...),
    data: str = Form(...),
    hora: str = Form(...),
    cliente: str = Form(...),
):
    novo_reservas = {
        "mesa_id": mesa_id,
        "data": data,
        "hora": hora,
        "cliente": cliente,
    }
    return add_reservas(novo_reservas)


@router.get("/reservas/editar/{reservas_id}")
def form_editar_reservas(request: Request, reservas_id: int):
    reservas = fetch_reservas_by_id(reservas_id)
    if not reservas:
        raise HTTPException(status_code=404, detail="reservas não encontrado")

    return templates.TemplateResponse(
        "form.html",
        {
            "request": request,
            "titulo": "Editar reservas",
            "url_salvar": f"/reservas/atualizar/{reservas_id}",
            "url_voltar": "/reservas",
            "campos": reservas,
        },
    )


@router.post("/reservas/atualizar/{reservas_id}")
def atualizar_reservas(
    reservas_id: int,
    mesa_id: int = Form(...),
    data: str = Form(...),
    hora: str = Form(...),
    cliente: str = Form(...),
):
    updated_data = {
        "mesa_id": mesa_id,
        "data": data,
        "hora": hora,
        "cliente": cliente,
    }
    return update_reservas_service(reservas_id, updated_data)


@router.get("/reservas/excluir/{reservas_id}")
def excluir_reservas(reservas_id: int):
    if delete_reservas_service(reservas_id):
        return {"message": "reservas deletado com sucesso"}
    raise HTTPException(status_code=404, detail="reservas não encontrado")
