from typing import Dict
from ..models.product import Product
from ..exceptions import InventoryInsufficientError

class Inventory:
    def __init__(self) -> None:
        self._products: Dict[str, Product] = {}

    def register(self, product: Product) -> None:
        self._products[product.id] = product

    def get(self, product_id: str) -> Product:
        return self._products[product_id]

    def ensure_available(self, product_id: str, qty: int) -> None:
        p = self.get(product_id)
        if p.stock < qty:
            raise InventoryInsufficientError(p.id, qty, p.stock)