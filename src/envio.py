class ServicoLogisticaAPI:
    def consultar_taxa(self, cep):
        raise NotImplementedError


class ServicoNotificacao:
    def enviar_notificacao_rastreio(self, pedido_id):
        raise NotImplementedError


def confirmar_frete(pedido_id, cep, usuario, logistica, notificacao):
    taxa = logistica.consultar_taxa(cep)
    notificacao.enviar_notificacao_rastreio(pedido_id)
    return taxa