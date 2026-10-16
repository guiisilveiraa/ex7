def calcular_frete(subtotal, regiao=None):
    if subtotal >= 250.00:
        frete = 0.00
    else:
        frete = 15.00

    if regiao in ("Norte", "Nordeste"):
        if subtotal > 300.00:
            return 0.00

        frete += 10.00

    return frete


def calcular_total(subtotal, regiao=None):
    return subtotal + calcular_frete(subtotal, regiao)