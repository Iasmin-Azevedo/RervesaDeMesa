from typing import List, Optional
import json

RESERVAS_FILE = "data/reservas.json"

def load_reservas():
    try:
        with open(RESERVAS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_reservas(reservas):
    with open(RESERVAS_FILE, "w") as f:
        json.dump(reservas, f, indent=4)

def fetch_reservas() -> List[dict]:
    return load_reservas()

def add_reservas(data: dict) -> dict:
    reservas = load_reservas()
    new_reserva = {
        "id": len(reservas) + 1,
        "mesa_id": data["mesa_id"],
        "data": data["data"],
        "hora": data["hora"],
        "cliente": data["cliente"],
    }
    reservas.append(new_reserva)
    save_reservas(reservas)
    return new_reserva

def update_reservas_service(reserva_id: int, data: dict) -> Optional[dict]:
    reservas = load_reservas()
    for reserva in reservas:
        if reserva["id"] == reserva_id:
            reserva.update(data)
            save_reservas(reservas)
            return reserva
    return None

def delete_reservas_service(reserva_id: int) -> bool:
    reservas = load_reservas()
    reservas_filtrados = [a for a in reservas if a["id"] != reserva_id]

    if len(reservas) == len(reservas_filtrados):
        return False

    save_reservas(reservas_filtrados)
    return True

def fetch_reservas_by_id(reserva_id: int) -> Optional[dict]:
    reservas = load_reservas()
    for reserva in reservas:
        if reserva["id"] == reserva_id:
            return reserva
    return None