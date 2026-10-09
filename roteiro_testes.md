# Exercício 7.1 — Roteiro de testes do checkout de frete

## Objetivo

Verificar o cálculo do frete e do total da compra por meio
de testes unitários, de integração e funcionais.

## Regras especificadas

REQ-01: o frete padrão é R$ 15,00, somado ao subtotal.

REQ-02: compras com subtotal maior ou igual a R$ 250,00
recebem frete grátis.

## Casos de teste

| ID | Tipo | Cenário | Entrada | Resultado esperado |
| --- | --- | --- | --- | --- |
| TU-01 | Unitário | Frete padrão | Subtotal de R$ 100,00 | Frete de R$ 15,00 |
| TU-02 | Unitário | Antigo limite de gratuidade | Subtotal de R$ 200,00 | Frete de R$ 15,00 |
| TU-03 | Unitário | Abaixo do novo limite | Subtotal de R$ 249,99 | Frete de R$ 15,00 |
| TU-04 | Unitário | Exatamente no novo limite | Subtotal de R$ 250,00 | Frete de R$ 0,00 |
| TU-05 | Unitário | Acima do novo limite | Subtotal de R$ 300,00 | Frete de R$ 0,00 |
| TU-06 | Unitário | Total com frete | Subtotal de R$ 100,00 | Total de R$ 115,00 |
| TU-07 | Unitário | Total no antigo limite | Subtotal de R$ 200,00 | Total de R$ 215,00 |
| TU-08 | Unitário | Total com frete grátis | Subtotal de R$ 250,00 | Total de R$ 250,00 |
| TI-01 | Integração | Checkout integrado ao cálculo de frete e total | Subtotal de R$ 100,00 | Frete de R$ 15,00 e total de R$ 115,00 |
| TI-02 | Integração | Checkout integrado com gratuidade | Subtotal de R$ 250,00 | Frete de R$ 0,00 e total de R$ 250,00 |
| TF-01 | Funcional | Executar a aplicação pelo terminal | Subtotal de R$ 100,00 | Exibir frete 15.00 e total 115.00 |
| TF-02 | Funcional | Executar a aplicação com frete grátis | Subtotal de R$ 250,00 | Exibir frete 0.00 e total 250.00 |

## Estratégia de execução

Os testes unitários verificam diretamente as funções
calcular_frete e calcular_total.

Os testes de integração verificam a função finalizar_compra,
que reúne o cálculo do frete e do total.

Os testes funcionais executam a aplicação pelo terminal
e verificam os valores apresentados ao usuário.

Os testes automatizados serão executados com pytest.
Os resultados serão registrados nos exercícios seguintes.

## Critério de aprovação

Todos os casos devem apresentar os resultados esperados,
respeitando REQ-01 e REQ-02.