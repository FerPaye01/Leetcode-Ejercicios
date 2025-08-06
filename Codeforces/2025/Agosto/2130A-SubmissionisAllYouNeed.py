"""import sys
 
def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    resultados = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index+n]))
        index += n
        suma_total = sum(arr)
        cantidad_ceros = arr.count(0)
        respuesta = suma_total + cantidad_ceros
        resultados.append(str(respuesta))
    
    print("\n".join(resultados))
 
if __name__ == "__main__":
    main()"""

import sys

def main():
    test_cases = [
        [0, 1, 1],        # Ejemplo 1: n=3
        [1, 2, 3],         # Ejemplo 2: n=3
        [0],               # Un solo cero
        [0, 0],            # Dos ceros
        [0, 0, 0],         # Tres ceros
        [0, 1],            # Cero y uno
        [0, 1, 2],         # Cero, uno y dos
        [0, 0, 1, 2],      # Dos ceros, uno y dos
        [1],               # Un solo uno (sin ceros)
        [0, 0, 1],         # Dos ceros y un uno
        [0]*50,            # 50 ceros
        [1]*50,            # 50 unos (sin ceros)
        list(range(50))    # Números del 0 al 49
    ]
    
    # Construir datos de entrada
    data = [str(len(test_cases))]
    for arr in test_cases:
        data.append(str(len(arr)))
        data.extend(map(str, arr))
    
    # Procesamiento de los datos
    t = int(data[0])
    index = 1
    resultados = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index+n]))
        index += n
        suma_total = sum(arr)
        cantidad_ceros = arr.count(0)
        respuesta = suma_total + cantidad_ceros
        resultados.append(str(respuesta))
    
    # Imprimir resultados
    print("\n".join(resultados))

if __name__ == "__main__":
    main()