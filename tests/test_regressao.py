import subprocess
import sys
from pathlib import Path

import pytest
from src.checkout import finalizar_compra


RAIZ = Path(__file__).resolve().parents[1]


def test_cupom_com_frete_padrao():
    frete, total = finalizar_compra(100, "DESCONTO10")

    assert frete == pytest.approx(15)
    assert total == pytest.approx(105)


def test_cupom_preserva_frete_gratis():
    frete, total = finalizar_compra(250, "DESCONTO10")

    assert frete == pytest.approx(0)
    assert total == pytest.approx(225)


def test_cupom_invalido():
    with pytest.raises(ValueError, match="Cupom invalido"):
        finalizar_compra(100, "OUTRO")


def test_aplicacao_com_cupom():
    resultado = subprocess.run(
        [
            sys.executable,
            "-m",
            "src.app",
            "100",
            "--cupom",
            "DESCONTO10",
        ],
        cwd=RAIZ,
        capture_output=True,
        text=True,
        timeout=10,
    )

    assert resultado.returncode == 0, resultado.stderr
    assert "Frete: 15.00" in resultado.stdout
    assert "Total: 105.00" in resultado.stdout