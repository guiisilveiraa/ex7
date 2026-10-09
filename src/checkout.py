from src.frete import calcular_frete, calcular_total


def finalizar_compra(subtotal):
    frete = calcular_frete(subtotal)
    total = calcular_total(subtotal)
    return frete, total