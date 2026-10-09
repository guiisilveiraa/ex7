import pytest
from src.checkout import finalizar_compra


def test_checkout_com_frete():
    frete, total = finalizar_compra(100)

    assert frete == pytest.approx(15)
    assert total == pytest.approx(115)


def test_checkout_com_frete_gratis():
    frete, total = finalizar_compra(250)

    assert frete == pytest.approx(0)
    assert total == pytest.approx(250)