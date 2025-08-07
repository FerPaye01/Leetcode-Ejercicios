"""import sys

def procesar_caso(datos):
    if not datos:
        return
    
    # Convertir los datos de entrada a enteros
    X = int(datos[0])
    Y = int(datos[1])
    
    # Calcular el total de monedas
    total_monedas = X * Y
    
    # Calcular las bolsas mediante división entera entre 100
    bolsas = total_monedas // 100
    
    # Imprimir el resultado
    print(bolsas)

def main():
    # Leer todos los datos de entrada
    datos = sys.stdin.read().split()
    
    # El primer dato es el número de casos de prueba (T)
    t = int(datos[0])
    
    # Índice para recorrer los datos
    indice = 1
    
    # Procesar cada caso de prueba
    for _ in range(t):
        # Cada caso de prueba tiene dos enteros: X e Y
        procesar_caso(datos[indice:indice + 2])
        indice += 2

if __name__ == "__main__":
    main()"""


import sys

def procesar_caso(datos):
    """
    Procesa un caso de prueba individual.
    
    Args:
        datos (list): Lista con los valores X e Y para el caso de prueba.
    """
    if not datos:
        return
    
    # Convertir los datos de entrada a enteros
    X = int(datos[0])
    Y = int(datos[1])
    
    # Calcular el total de monedas obtenidas
    total_monedas = X * Y
    
    # Calcular las bolsas mediante división entera entre 100
    bolsas = total_monedas // 100
    
    # Imprimir el resultado
    print(bolsas)

def main():
    # Verificar si la entrada es interactiva (terminal)
    if sys.stdin.isatty():
        # Modo de prueba local: usar casos de prueba predefinidos
        test_cases = [
            (10, 10),  # 10*10 = 100 -> 1 bolsa
            (20, 4),    # 20*4 = 80   -> 0 bolsas
            (70, 7),    # 70*7 = 490  -> 4 bolsas
            (1, 1000),  # 1*1000 = 1000 -> 10 bolsas
            (1000, 1),  # 1000*1 = 1000 -> 10 bolsas
            (99, 99),   # 99*99 = 9801 -> 98 bolsas
            (100, 1),   # 100*1 = 100 -> 1 bolsa
            (50, 2)     # 50*2 = 100 -> 1 bolsa
        ]
        # Convertir los casos de prueba a lista de strings
        data = [str(len(test_cases))]
        for X, Y in test_cases:
            data.append(str(X))
            data.append(str(Y))
    else:
        # Leer todos los datos de entrada estándar
        data = sys.stdin.read().split()
    
    # El primer elemento es el número de casos de prueba
    t = int(data[0])
    indice = 1
    
    # Procesar cada caso de prueba
    for _ in range(t):
        # Cada caso de prueba tiene dos valores: X e Y
        procesar_caso(data[indice:indice+2])
        indice += 2

if __name__ == "__main__":
    main()