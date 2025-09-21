from dataclasses import dataclass, field
from typing import Dict
from ..exceptions import InventoryInsufficientError, InvalidOperationError
from .product import Product

@dataclass
class CartItem:
    product: Product
    quantity: int

    @property
    def subtotal(self) -> float:
        return self.product.price * self.quantity

@dataclass
class Cart:
    items: Dict[str, CartItem] = field(default_factory=dict)

    def add_product(self, product: Product, qty: int = 1) -> None:
        if qty <= 0:
            raise InvalidOperationError("La cantidad debe ser mayor que cero")
        if product.stock < qty:
            raise InventoryInsufficientError(product.id, qty, product.stock)
        # reduce stock first to keep invariants
        product.reduce_stock(qty)
        if product.id in self.items:
            self.items[product.id].quantity += qty
        else:
            self.items[product.id] = CartItem(product, qty)

    def remove_product(self, product_id: str, qty: int = None) -> None:
        if product_id not in self.items:
            raise InvalidOperationError("El producto no está en el carrito")
        item = self.items[product_id]
        if qty is None or qty >= item.quantity:
            # return stock
            item.product.increase_stock(item.quantity)
            del self.items[product_id]
        else:
            item.product.increase_stock(qty)
            item.quantity -= qty

    def total(self) -> float:
        return sum(ci.subtotal for ci in self.items.values())

    def clear(self) -> None:
        # return stock for all items
        for item in list(self.items.values()):
            item.product.increase_stock(item.quantity)
        self.items.clear()