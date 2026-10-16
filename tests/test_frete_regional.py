import pytest
from src.frete import calcular_frete, calcular_total


@pytest.mark.parametrize(
    "regiao, subtotal, esperado",
    [
        ("Norte", 100.00, 25.00),
        ("Nordeste", 100.00, 25.00),
        ("Norte", 250.00, 10.00),
        ("Nordeste", 250.00, 10.00),
        ("Norte", 300.00, 10.00),
        ("Nordeste", 300.00, 10.00),
        ("Norte", 300.01, 0.00),
        ("Nordeste", 300.01, 0.00),
        ("Sudeste", 100.00, 15.00),
        ("Sul", 250.00, 0.00),
    ],
)
def test_frete_regional(regiao, subtotal, esperado):
    # Arrange
    valor_carrinho = subtotal
    regiao_entrega = regiao

    # Act
    resultado = calcular_frete(valor_carrinho, regiao_entrega)

    # Assert
    assert resultado == pytest.approx(esperado)


def test_total_com_adicional_regional():
    # Arrange
    subtotal = 100.00
    regiao = "Norte"
    esperado = 125.00

    # Act
    resultado = calcular_total(subtotal, regiao)

    # Assert
    assert resultado == pytest.approx(esperado)