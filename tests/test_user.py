from ecommerce.models.user import User

def test_masked_email():
    u = User(id="U1", name="Ana", email="ana.rodriguez@example.com")
    masked = u.masked_email()
    assert masked.endswith("@example.com")
    assert "***" in masked