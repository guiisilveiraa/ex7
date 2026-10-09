import argparse
from src.checkout import finalizar_compra


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("subtotal", type=float)
    parser.add_argument("--cupom", default=None)
    argumentos = parser.parse_args()

    try:
        frete, total = finalizar_compra(
            argumentos.subtotal,
            argumentos.cupom,
        )
    except ValueError as erro:
        parser.error(str(erro))

    print(f"Frete: {frete:.2f}")
    print(f"Total: {total:.2f}")


if __name__ == "__main__":
    main()