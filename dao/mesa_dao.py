import json

MESAS_FILE = "data/mesas.json"


def load_mesas():
    """Carrega as mesas do arquivo JSON."""
    try:
        with open(MESAS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_mesas(mesas):
    """Salva as mesas no arquivo JSON."""
    with open(MESAS_FILE, "w") as file:
        json.dump(mesas, file, indent=4)


def get_all_mesas():
    """Retorna todas as mesas cadastradas."""
    return load_mesas()


def get_mesa_by_id(mesa_id):
    """Busca uma mesa específica pelo ID."""
    mesas = load_mesas()
    for mesa in mesas:
        if mesa["id"] == mesa_id:
            return mesa
    return None


def insert_mesa(mesa):
    """Insere uma nova mesa no sistema."""
    mesas = load_mesas()
    mesa["id"] = len(mesas) + 1  # Simula um ID autoincremento
    mesas.append(mesa)
    save_mesas(mesas)
    return mesa


def update_mesa(mesa_atualizada):
    """Atualiza uma mesa existente."""
    mesas = load_mesas()
    for i, mesa in enumerate(mesas):
        if mesa["id"] == mesa_atualizada["id"]:
            mesas[i] = mesa_atualizada
            save_mesas(mesas)
            return mesa_atualizada
    return None


def delete_mesa(mesa_id):
    """Remove uma mesa pelo ID."""
    mesas = load_mesas()
    mesas_filtradas = [q for q in mesas if q["id"] != mesa_id]

    if len(mesas) == len(mesas_filtradas):
        return False  # Nenhuma mesa removida

    save_mesas(mesas_filtradas)
    return True  # Sucesso
