# Exercício 2 — Auditoria de Drift

## Ferramentas utilizadas

ChatGPT auxiliou na geração e revisão do código candidato.
Os testes foram executados no terminal do PyCharm.

## Experimento

Foi adicionada temporariamente uma funcionalidade que aceita
o cupom DESCONTO10 e aplica desconto de 10% sobre o frete.

A especificação permaneceu com apenas REQ-01 e REQ-02,
sem autorizar cupons.

## Matriz de rastreabilidade

| Requisito | Código candidato | Testes existentes |
| --- | --- | --- |
| REQ-01: frete padrão de R$ 15,00 | Atendido sem cupom; violado com DESCONTO10 | test_frete_padrao e test_total_com_frete |
| REQ-02: frete grátis para subtotal >= R$ 200,00 | Atendido | test_frete_gratis e test_total_sem_frete |
| Cupom DESCONTO10 | Funcionalidade sem requisito: drift | Nenhum teste existente cobre o cupom |

## Desvio identificado

Para subtotal de R$ 100,00 e cupom DESCONTO10,
o código candidato retornou frete de R$ 13,50.

Entretanto, REQ-01 determina frete de R$ 15,00 nessa situação.
Logo, a funcionalidade de cupom constitui sobre-implementação.

Os quatro testes existentes passaram mesmo com o desvio,
porque nenhum deles utilizava o parâmetro de cupom.
Isso demonstra a necessidade de revisar a rastreabilidade
entre especificação, implementação e testes.

## Correção realizada

Foram removidos o parâmetro cupom e a lógica de desconto
das funções calcular_frete e calcular_total.

O código final implementa somente REQ-01 e REQ-02.

## Revisão multidimensional

Arquitetura: duas funções simples, sem dependências externas.

Performance: cálculo com tempo e espaço constantes, sem loops.

Segurança: não há exposição de dados sensíveis. A implementação
pressupõe subtotal numérico, finito e não negativo. A ausência
de validação dessas entradas foi registrada como limitação.

Observabilidade: nomes claros e referências aos requisitos
nas docstrings. Não há registro de eventos em execução.

## Resultado

Antes da correção: quatro testes aprovados, mas o cálculo
manual com cupom revelou frete de R$ 13,50.

Após a correção: os quatro testes foram novamente aprovados
e a funcionalidade não especificada foi removida.