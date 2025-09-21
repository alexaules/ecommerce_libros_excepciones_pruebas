
from ecommerce.models.product import Product
from ecommerce.models.cart import Cart
from ecommerce.models.user import User
from ecommerce.services.payment import PaymentGateway
from ecommerce.exceptions import InventoryInsufficientError, PaymentFailedError

def main():
    # Crear productos y usuario
    libro = Product(id="L001", name="Python Básico", price=25.0, stock=5)
    usuario = User(id="U001", name="Ana Pérez", email="ana@example.com")
    carrito = Cart()

    print(f"Usuario: {usuario.name} ({usuario.masked_email()})")
    print(f"Stock inicial del libro '{libro.name}': {libro.stock}")

    # Agregar producto al carrito
    try:
        carrito.add_product(libro, 3)
        print(f"Se agregaron 3 unidades. Total: {carrito.total()}€")
    except InventoryInsufficientError as e:
        print(f"Error de inventario: {e}")

    # Intentar agregar más de lo disponible para provocar excepción
    try:
        carrito.add_product(libro, 5)
    except InventoryInsufficientError as e:
        print(f"Excepción capturada correctamente: {e}")

    # Procesar pago
    gateway = PaymentGateway(success=True)
    try:
        auth_code = gateway.charge(carrito.total())
        print(f"Pago exitoso. Código de autorización: {auth_code}")
    except PaymentFailedError as e:
        print(f"Error en el pago: {e}")

if __name__ == "__main__":
    main()
