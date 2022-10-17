class Destino:
    def __init__(self, ddd: int, destino: str) -> None:
        self.ddd = ddd
        self.destino = destino

    def __eq__(self, other) -> bool:
        return self.ddd == other.ddd and self.destino == other.destino