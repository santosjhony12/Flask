class Tarefa:
    def __init__(self, id=None, titulo=None, feito=None):
        self.id = id
        self.titulo = titulo
        self.feito = feito

    def to_dict(self):
        return {"id": str(self.id), "titulo": self.titulo, "feito": self.feito}