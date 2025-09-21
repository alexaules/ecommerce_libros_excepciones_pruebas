import pytest
from ecommerce.services.payment import PaymentGateway
from ecommerce.exceptions import PaymentFailedError

def test_payment_success_returns_auth_code():
    gw = PaymentGateway(success=True)
    code = gw.charge(100.0)
    assert code.startswith("AUTH-")

def test_payment_declined_raises():
    gw = PaymentGateway(success=False, decline_reason="Fondos insuficientes")
    with pytest.raises(PaymentFailedError):
        gw.charge(55.0)

def test_payment_invalid_amount():
    gw = PaymentGateway()
    with pytest.raises(PaymentFailedError):
        gw.charge(0.0)