# Exercício 7.5 — Testes de regressão

## Nova funcionalidade

Foi implementado o cupom DESCONTO10, que concede desconto
de 10% sobre o subtotal dos produtos.

O frete é calculado utilizando o subtotal original.
Cupons diferentes de DESCONTO10 são rejeitados.

A especificação foi atualizada antes da implementação,
com a inclusão de REQ-03 e REQ-04.

## Procedimento e resultados

Antes da mudança, os 12 testes existentes foram aprovados.

Após adicionar os quatro testes novos, mas antes de implementar
o cupom, foram obtidos 12 testes aprovados e 4 falhas.

Após implementar o cupom, todos os 16 testes foram aprovados.

## Evidências

- resultados_antes_da_mudanca.txt
- resultados_novos_testes_antes.txt
- resultados_regressao.txt

## Conclusão

Os testes anteriores continuaram aprovados após a alteração.

Os novos testes verificaram o desconto, a preservação do
frete grátis, a rejeição de cupom inválido e a execução
da aplicação com cupom.