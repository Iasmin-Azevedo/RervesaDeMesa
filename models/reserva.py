class Reserva:
    def __init__(self, id: int, mesa_id: int, data: str, hora: str, nome_responsavel: str):
        self.id = id
        self.mesa_id = mesa_id
        self.data = data
        self.hora = hora
        self.cliente = nome_responsavel

    def to_dict(self):
        return {
            "id": self.id,
            "mesa_id": self.mesa_id,
            "data": self.data,
            "hora": self.hora,
            "cliente": self.nome_responsavel
        }