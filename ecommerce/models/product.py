from dataclasses import dataclass, field

@dataclass
class Product:
    id: str
    name: str
    price: float
    stock: int = field(default=0)

    def reduce_stock(self, qty: int) -> None:
        if qty < 0:
            raise ValueError("qty debe ser >= 0")
        if qty > self.stock:
            raise ValueError("No hay stock suficiente para reducir")
        self.stock -= qty

    def increase_stock(self, qty: int) -> None:
        if qty < 0:
            raise ValueError("qty debe ser >= 0")
        self.stock += qty