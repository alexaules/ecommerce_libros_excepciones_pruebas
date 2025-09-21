from dataclasses import dataclass
from ..exceptions import PaymentFailedError

@dataclass
class PaymentGateway:
    """Fake gateway to simulate payment outcomes."""
    success: bool = True
    decline_reason: str = "Tarjeta rechazada"

    def charge(self, amount: float) -> str:
        if amount <= 0:
            raise PaymentFailedError("El monto debe ser mayor a 0")
        if not self.success:
            raise PaymentFailedError(self.decline_reason)
        # return a fake authorization code
        return "AUTH-" + str(abs(hash((amount, self.success))) % 10_000_000)