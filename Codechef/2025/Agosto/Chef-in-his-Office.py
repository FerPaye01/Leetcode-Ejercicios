import sys

def procesar_caso(datos):
    """
    Calcula las horas totales trabajadas en una semana.
    
    Parámetros:
    datos -- lista con dos strings: [X, Y]
    
    Retorna:
    total -- horas totales de trabajo semanal (entero)
    """
    # Convertir los valores de entrada a enteros
    X = int(datos[0])  # Horas diarias de lunes a jueves
    Y = int(datos[1])  # Horas del viernes
    
    # Calcular total: 4 días * X horas + 1 día * Y horas
    total = 4 * X + Y
    return total

def main():
    """
    Función principal que maneja la entrada y ejecuta los casos de prueba.
    """
    # Verificar si la entrada es interactiva (terminal) o por redirección
    if sys.stdin.isatty():
        # Modo de prueba local: ejecutar casos de prueba predefinidos
        print("Modo de prueba: ejecutando casos predefinidos\n")
        
        # Casos de prueba del problema + adicionales
        casos_prueba = [
            ["10", "5"],  # 4*10 + 5 = 45
            ["12", "2"],  # 4*12 + 2 = 50
            ["8", "7"],   # 4*8 + 7 = 39
            ["2", "1"],   # 4*2 + 1 = 9 (caso mínimo)
            ["12", "1"],  # 4*12 + 1 = 49 (caso máximo)
            ["5", "3"],   # 4*5 + 3 = 23
            ["9", "4"]    # 4*9 + 4 = 40
        ]
        
        # Procesar cada caso de prueba
        for i, caso in enumerate(casos_prueba, 1):
            print(f"Caso de prueba #{i}: X={caso[0]}, Y={caso[1]}")
            resultado = procesar_caso(caso)
            print(f"Resultado: {resultado}\n")
    else:
        # Modo de competición: leer datos de entrada estándar
        data = sys.stdin.read().split()  # Leer todos los datos de entrada
        
        # El primer elemento es el número de casos de prueba (T)
        t = int(data[0])
        indice = 1  # Índice para recorrer los datos
        resultados = []
        
        # Procesar cada caso de prueba
        for _ in range(t):
            # Tomar los siguientes dos valores: X e Y
            caso = data[indice:indice + 2]
            indice += 2  # Avanzar el índice para el próximo caso
            
            # Calcular y almacenar resultado
            resultado = procesar_caso(caso)
            resultados.append(str(resultado))
        
        # Imprimir todos los resultados (uno por línea)
        print("\n".join(resultados))

if __name__ == "__main__":

    main()