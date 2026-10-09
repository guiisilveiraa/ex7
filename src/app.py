import argparse
from src.checkout import finalizar_compra


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("subtotal", type=float)
    argumentos = parser.parse_args()

    frete, total = finalizar_compra(argumentos.subtotal)

    print(f"Frete: {frete:.2f}")
    print(f"Total: {total:.2f}")


if __name__ == "__main__":
    main()