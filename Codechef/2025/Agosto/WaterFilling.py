import sys

# Mensajes constantes (evitan "magic strings" repetidos)
MSG_RELLENAR = "Water filling time"
MSG_NO = "Not now"

def procesar_entrada(tokens):
    """
    tokens: lista de cadenas resultado de sys.stdin.read().split()
    Formato esperado:
      tokens[0] = T
      luego T * 3 enteros (B1 B2 B3) por caso.
    """
    if not tokens:
        return

    idx = 0
    try:
        T = int(tokens[idx]); idx += 1
    except Exception:
        # entrada inválida o vacía
        return

    salida = []  # acumulamos salidas y al final imprimimos con join (más rápido)

    for _ in range(T):
        # Si faltan tokens, salimos limpiamente
        if idx + 2 >= len(tokens):
            break

        # Leemos las tres botellas; variables en español
        botella1 = int(tokens[idx]); botella2 = int(tokens[idx + 1]); botella3 = int(tokens[idx + 2])
        idx += 3

        # Contamos vacías: dado que Bi ∈ {0,1}, vacías = 3 - suma
        suma_llenas = botella1 + botella2 + botella3
        vacias = 3 - suma_llenas

        # Condición: si al menos dos están vacías -> rellenar
        if vacias >= 2:
            salida.append(MSG_RELLENAR)
        else:
            salida.append(MSG_NO)

    # Imprimimos todas las respuestas, una por línea
    sys.stdout.write("\n".join(salida))

def main():
    if sys.stdin.isatty():
        # Modo de prueba local (casos de ejemplo del enunciado)
        casos_prueba = [
            "5 0 0 0 1 1 1 1 1 0 0 1 0 0 1 1".split(),  # conjunto de 5 casos (ejemplo)
            # otros pequeños conjuntos para verificar bordes
            "3 0 0 1 0 1 1".split(),  # 3 casos: (0,0,1)->Yes, (0,1,0)->Yes, (1,1,?) incomplete
        ]
        for tokens in casos_prueba:
            print("--- Ejecutando caso de prueba simulado ---")
            procesar_entrada(tokens)
            print()
    else:
        data = sys.stdin.read().split()
        procesar_entrada(data)

if __name__ == "__main__":
    main()
