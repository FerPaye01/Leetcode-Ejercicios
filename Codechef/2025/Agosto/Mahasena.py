import sys

def procesar_caso(data):
    """
    Procesa un caso de prueba para determinar si el ejército está listo para la batalla.
    
    Args:
        data (list): Lista de strings con los datos del caso.
            data[0] = número de soldados (N)
            data[1:1+N] = armas de cada soldado (A1, A2, ..., AN)
    
    Realiza:
        1. Convierte los datos a enteros
        2. Cuenta soldados con armas pares (afortunados)
        3. Determina si los afortunados > desafortunados
        4. Imprime "READY FOR BATTLE" o "NOT READY"
    """
    if not data:
        return
    
    # Convertir primer elemento a entero (número de soldados)
    n = int(data[0])
    # Convertir siguientes n elementos a enteros (armas de los soldados)
    armas = list(map(int, data[1:1+n]))
    
    # Contar soldados con número par de armas (afortunados)
    afortunados = 0
    for num in armas:
        # Un número es par si el residuo al dividir por 2 es 0
        if num % 2 == 0:
            afortunados += 1
    
    # Calcular soldados con armas impares (desafortunados)
    desafortunados = n - afortunados
    
    # Determinar preparación del ejército
    if afortunados > desafortunados:
        print("READY FOR BATTLE")
    else:
        print("NOT READY")

def main():
    """
    Función principal que maneja la entrada de datos:
    - En modo interactivo (terminal): ejecuta casos de prueba predefinidos
    - En modo no interactivo (archivo/pipe): lee datos de stdin
    
    Casos de prueba incluidos (del problema y adicionales):
        1. 1 soldado con 1 arma -> NOT READY
        2. 1 soldado con 2 armas -> READY FOR BATTLE
        3. 4 soldados: [11,12,13,14] -> NOT READY
        4. 3 soldados: [2,3,4] -> READY FOR BATTLE
        5. 5 soldados: [1,2,3,4,5] -> NOT READY
        6. 2 soldados: [10,15] -> NOT READY
        7. 2 soldados: [10,20] -> READY FOR BATTLE
        8. 3 soldados: [100,100,100] -> READY FOR BATTLE
        9. 0 soldados (inválido por restricciones) -> omitido
    """
    if sys.stdin.isatty():
        # Modo de prueba local: ejecutar casos de prueba predefinidos
        test_cases = [
            ["1", "1"],                 # NOT READY
            ["1", "2"],                 # READY FOR BATTLE
            ["4", "11", "12", "13", "14"], # NOT READY
            ["3", "2", "3", "4"],       # READY FOR BATTLE
            ["5", "1", "2", "3", "4", "5"], # NOT READY
            ["2", "10", "15"],          # NOT READY
            ["2", "10", "20"],          # READY FOR BATTLE
            ["3", "100", "100", "100"]  # READY FOR BATTLE
        ]
        for tokens in test_cases:
            print(f"--- Caso de prueba: {tokens} ---")
            procesar_caso(tokens)
            print()
    else:
        # Leer datos de entrada estándar (archivo/pipe)
        data = sys.stdin.read().split()
        procesar_caso(data)

if __name__ == "__main__":
    main()