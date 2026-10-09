def calcular_desconto(subtotal, cupom=None):
    if cupom is None:
        return 0.00

    if cupom != "DESCONTO10":
        raise ValueError("Cupom invalido")

    return subtotal * 0.10