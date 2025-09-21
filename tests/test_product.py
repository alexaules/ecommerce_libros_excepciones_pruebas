import pytest
from ecommerce.models.product import Product

def test_increase_and_reduce_stock_ok():
    p = Product(id="B001", name="Libro 1", price=10.0, stock=5)
    p.increase_stock(3)
    assert p.stock == 8
    p.reduce_stock(5)
    assert p.stock == 3

def test_reduce_stock_raises_on_insufficient():
    p = Product(id="B002", name="Libro 2", price=12.0, stock=1)
    with pytest.raises(ValueError):
        p.reduce_stock(2)