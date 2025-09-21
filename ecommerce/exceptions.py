class ECommerceError(Exception):
    """Base class for e-commerce domain errors."""

class InventoryInsufficientError(ECommerceError):
    def __init__(self, product_id: str, requested: int, available: int):
        super().__init__(
            f"Inventario insuficiente para producto '{product_id}': "
            f"solicitado={requested}, disponible={available}"
        )
        self.product_id = product_id
        self.requested = requested
        self.available = available

class PaymentFailedError(ECommerceError):
    def __init__(self, reason: str = "Pago rechazado"):
        super().__init__(f"Pago fallido: {reason}")
        self.reason = reason

class UserNotFoundError(ECommerceError):
    def __init__(self, user_id: str):
        super().__init__(f"Usuario no encontrado: {user_id}")
        self.user_id = user_id

class InvalidOperationError(ECommerceError):
    """Raised when an operation is not allowed or invalid in domain."""
    def __init__(self, message: str):
        super().__init__(message)