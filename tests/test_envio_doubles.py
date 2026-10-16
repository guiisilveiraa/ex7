from unittest.mock import Mock

import pytest

from src.envio import (
    ServicoLogisticaAPI,
    ServicoNotificacao,
    confirmar_frete,
)


def test_confirmar_frete_com_test_doubles():
    # Arrange
    pedido_id = "PEDIDO-123"
    cep = "04101000"

    # Dummy: preenche o parametro sem participar da logica
    usuario_dummy = object()

    # Stub: fornece uma taxa fixa sem chamada de rede
    logistica_stub = Mock(spec=ServicoLogisticaAPI)
    logistica_stub.consultar_taxa.return_value = 15.00

    # Mock: registra chamadas para verificacao
    notificacao_mock = Mock(spec=ServicoNotificacao)

    # Act
    taxa = confirmar_frete(
        pedido_id,
        cep,
        usuario_dummy,
        logistica_stub,
        notificacao_mock,
    )

    # Assert
    assert taxa == pytest.approx(15.00)
    logistica_stub.consultar_taxa.assert_called_once_with(cep)
    notificacao_mock.enviar_notificacao_rastreio.assert_called_once_with(
        pedido_id
    )