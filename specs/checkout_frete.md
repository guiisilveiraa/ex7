REQ-01: THE SYSTEM SHALL calcular o valor total adicionando a taxa de frete padrão de R$ 15,00 ao subtotal do carrinho, exceto quando houver frete grátis conforme REQ-02 e desconto conforme REQ-03.

REQ-02: IF o subtotal original do carrinho for maior ou igual a R$ 250,00, THEN THE SYSTEM SHALL conceder frete grátis, com taxa de R$ 0,00.

REQ-03: WHEN o usuário informar o cupom DESCONTO10, THE SYSTEM SHALL aplicar desconto de 10% sobre o subtotal dos produtos, mantendo o cálculo do frete baseado no subtotal original.

REQ-04: IF um cupom diferente de DESCONTO10 for informado, THEN THE SYSTEM SHALL rejeitar o cupom com a mensagem "Cupom invalido".