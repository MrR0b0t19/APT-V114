# Este archivo Python nos funciona para leer la ruleta rusa de los participantes del GIVEAWAY
# espero les guste y acepten 

import argparse
import random
import sys
import time

def cargar_participantes(archivo):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            nombres = [line.strip() for line in f if line.strip()]
        return nombres
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo: {archivo}")
        sys.exit(1)

def main():

    seed = time.time_ns() % 10000

    random.seed(seed)

    parser = argparse.ArgumentParser(
        description="Ruleta rusa: selecciona un ganador al azar"
    )

    parser.add_argument(
        "archivo",
        help="Archivo TXT con la lista de participantes"
    )

    args = parser.parse_args()

    participantes = cargar_participantes(args.archivo)

    if len(participantes) == 0:
        print("Error: El archivo no contiene participantes")
        sys.exit(1)

    ganador = random.choice(participantes)

    print("==============================================")
    print("=     EL GANADOR ES:      ", ganador)
    print("==============================================")


if __name__ == "__main__":
    main()

