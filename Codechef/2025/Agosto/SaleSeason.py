import sys

def procesar_caso(tokens):
    # tokens: lista de strings que contienen T seguido de T valores X
    if not tokens:
        return

    # número de casos
    t = int(tokens[0])
    salida = []  # acumulador de resultados para salida en bloque
    idx = 1      # índice actual en tokens

    for _ in range(t):
        # leer el gasto X (asegura que haya tokens suficientes)
        if idx >= len(tokens):
            break
        gasto = int(tokens[idx]); idx += 1

        # determinar descuento según rangos especificados
        if gasto <= 100:
            descuento = 0
        elif gasto <= 1000:      # 100 < gasto <= 1000
            descuento = 25
        elif gasto <= 5000:      # 1000 < gasto <= 5000
            descuento = 100
        else:                    # gasto > 5000
            descuento = 500

        # calcular total final y añadir a salida
        total_final = gasto - descuento
        salida.append(str(total_final))

    # imprimir todos los resultados, un por línea
    sys.stdout.write("\n".join(salida) + ("\n" if salida else ""))


def main():
    # Si se ejecuta localmente desde terminal, usar casos de prueba integrados
    if sys.stdin.isatty():
        casos_prueba = [
            ["4", "15", "70", "250", "1000"],   # ejemplo del enunciado
            ["3", "100", "101", "5001"],        # borde 100, >100, >5000
            ["5", "1", "1000", "1001", "5000", "5001"]  # varios bordes
        ]
        for tokens in casos_prueba:
            print(f"--- Caso de prueba: {tokens} ---")
            procesar_caso(tokens)
            print()
    else:
        # Leer entrada estándar, dividir por espacios/nuevas líneas y procesar
        datos = sys.stdin.read().split()
        procesar_caso(datos)


if __name__ == "__main__":
    main()
