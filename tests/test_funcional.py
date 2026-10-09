import subprocess
import sys
from pathlib import Path


RAIZ = Path(__file__).resolve().parents[1]


def test_aplicacao_com_frete():
    resultado = subprocess.run(
        [sys.executable, "-m", "src.app", "100"],
        cwd=RAIZ,
        capture_output=True,
        text=True,
        timeout=10,
    )

    assert resultado.returncode == 0, resultado.stderr
    assert "Frete: 15.00" in resultado.stdout
    assert "Total: 115.00" in resultado.stdout


def test_aplicacao_com_frete_gratis():
    resultado = subprocess.run(
        [sys.executable, "-m", "src.app", "250"],
        cwd=RAIZ,
        capture_output=True,
        text=True,
        timeout=10,
    )

    assert resultado.returncode == 0, resultado.stderr
    assert "Frete: 0.00" in resultado.stdout
    assert "Total: 250.00" in resultado.stdout