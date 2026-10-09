from src.desconto import calcular_desconto
from src.frete import calcular_frete, calcular_total


def finalizar_compra(subtotal, cupom=None):
    desconto = calcular_desconto(subtotal, cupom)
    frete = calcular_frete(subtotal)
    total = calcular_total(subtotal) - desconto

    return frete, total