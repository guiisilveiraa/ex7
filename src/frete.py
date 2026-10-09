def calcular_frete(subtotal):
    """REQ-01: taxa padrão. REQ-02: frete grátis."""
    if subtotal >= 250.00:
        return 0.00
    return 15.00


def calcular_total(subtotal):
    """REQ-01 e REQ-02: subtotal somado ao frete."""
    return subtotal + calcular_frete(subtotal)