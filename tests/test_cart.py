import pytest
from ecommerce.models.product import Product
from ecommerce.models.cart import Cart
from ecommerce.exceptions import InventoryInsufficientError, InvalidOperationError

def test_add_product_ok_and_total():
    p = Product(id="B003", name="Libro 3", price=15.0, stock=10)
    c = Cart()
    c.add_product(p, 2)
    assert c.total() == 30.0
    assert p.stock == 8

def test_add_product_invalid_qty():
    p = Product(id="B004", name="Libro 4", price=20.0, stock=5)
    c = Cart()
    with pytest.raises(InvalidOperationError):
        c.add_product(p, 0)

def test_add_product_insufficient_stock():
    p = Product(id="B005", name="Libro 5", price=8.0, stock=1)
    c = Cart()
    with pytest.raises(InventoryInsufficientError):
        c.add_product(p, 2)

def test_remove_product_returns_stock():
    p = Product(id="B006", name="Libro 6", price=9.0, stock=3)
    c = Cart()
    c.add_product(p, 2)
    c.remove_product("B006", 1)
    assert c.total() == 9.0
    assert p.stock == 2  # 3 -2 +1
    c.remove_product("B006")
    assert c.total() == 0.0
    assert p.stock == 3

def test_clear_returns_all_stock():
    p = Product(id="B007", name="Libro 7", price=7.0, stock=5)
    c = Cart()
    c.add_product(p, 3)
    c.clear()
    assert p.stock == 5
    assert c.total() == 0.0