import sys                                         # importo sys para lectura eficiente de entrada/salida

def procesar_entrada(tokens):                      # función que procesa todos los tokens de entrada
    if not tokens:                                  # si no hay tokens, no hay nada que procesar
        return
    ptr = 0                                         # puntero a la posición actual en la lista de tokens
    t_casos = int(tokens[ptr]); ptr += 1            # número de casos de prueba (T)
    resultado = []                                  # lista para acumular las respuestas como strings
    for _ in range(t_casos):                        # itero por cada caso de prueba
        amigos = int(tokens[ptr]); ptr += 1         # número de amigos N
        porciones_por_amigo = int(tokens[ptr]); ptr += 1  # porciones que quiere cada amigo X
        total_porciones = amigos * porciones_por_amigo   # número total de porciones requeridas
        # aplico división entera hacia arriba: ceil(total_porciones / 4)
        pizzas = (total_porciones + 4 - 1) // 4     # calculo mínimo de pizzas (cada pizza tiene 4 slices)
        resultado.append(str(pizzas))               # almaceno el resultado (como string) para salida
    sys.stdout.write("\n".join(resultado))          # imprimo todas las respuestas separadas por saltos de línea

def main():                                        # función principal que decide modo prueba o modo concurso
    if sys.stdin.isatty():                         # si la entrada es interactiva (modo local / pruebas)
        # casos de prueba locales (mismo formato que en el enunciado)
        datos_prueba = """4
1 5
2 6
4 3
3 5
""".split()
        print("--- Ejecutando pruebas locales ---")# indico que son pruebas locales
        procesar_entrada(datos_prueba)             # proceso las pruebas de ejemplo
    else:
        tokens = sys.stdin.read().split()          # leo todo desde stdin y lo separo en tokens
        procesar_entrada(tokens)                   # proceso la entrada provista por el juez/archivo

if __name__ == "__main__":                        # punto de entrada del script
    main()                                        # llamo a main()
