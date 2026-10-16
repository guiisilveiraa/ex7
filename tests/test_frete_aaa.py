import pytest
from src.frete import calcular_frete


@pytest.mark.parametrize(
    "subtotal, frete_esperado",
    [
        (100.00, 15.00),
        (249.99, 15.00),
        (250.00, 0.00),
        (300.00, 0.00),
    ],
)
def test_calcular_frete_padrao_aaa(subtotal, frete_esperado):
    # Arrange: preparar os dados
    valor_carrinho = subtotal
    valor_esperado = frete_esperado

    # Act: executar a operacao
    resultado = calcular_frete(valor_carrinho)

    # Assert: verificar o resultado
    assert resultado == pytest.approx(valor_esperado)