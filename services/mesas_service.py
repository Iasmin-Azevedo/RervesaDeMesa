from dao.mesa_dao import (
    get_all_mesas,
    get_mesa_by_id,
    insert_mesa,
    update_mesa,
    delete_mesa,
)

def fetch_mesas():
    """Retorna todas as mesas cadastradas."""
    return get_all_mesas()

def fetch_mesas_by_id(mesa_id: int):
    """Busca uma mesa específica pelo ID."""
    return get_mesa_by_id(mesa_id)

def add_mesas(data: dict):
    """Adiciona uma nova mesa ao sistema."""
    nova_mesa = {
        "id": None,  # Será gerado automaticamente no DAO
        "nome": data["nome"],
        "capacidade": data["capacidade"],
    }
    return insert_mesa(nova_mesa)

def update_mesas_service(mesa_id: int, data: dict):
    """Atualiza uma mesa existente."""
    mesa_existente = get_mesa_by_id(mesa_id)
    if not mesa_existente:
        return None  # Mesa não encontrada

    mesa_atualizada = {
        "id": mesa_id,
        "nome": data["nome"],
        "capacidade": data["capacidade"],
    }
    return update_mesa(mesa_atualizada)

def delete_mesas_service(mesa_id: int):
    """Exclui uma mesa pelo ID."""
    return delete_mesa(mesa_id)