import sys

def main():
    if sys.stdin.isatty():
        # Modo de prueba local: usar casos de prueba predefinidos
        test_cases = [
            (2, 10, 12),    # 12/20 = 60% -> YES
            (2, 10, 3),     # 3/20 = 15% -> NO
            (1, 5, 3),      # 3/5 = 60% -> YES
            (3, 6, 9),      # 9/18 = 50% -> NO
            (1, 1, 1),      # 1/1 = 100% -> YES
            (5, 50, 125),   # 125/250 = 50% -> NO
            (1, 50, 0),     # 0/50 = 0% -> NO
            (3, 10, 16),    # 16/30 ≈ 53.3% -> YES
            (4, 25, 51),    # 51/100 = 51% -> YES
            (5, 20, 49)     # 49/100 = 49% -> NO
        ]
        data = [str(len(test_cases))]
        for X, Y, Z in test_cases:
            data.append(str(X))
            data.append(str(Y))
            data.append(str(Z))
    else:
        # Leer datos de entrada estándar
        data = sys.stdin.read().split()
    
    t = int(data[0])
    index = 1
    resultados = []
    
    for _ in range(t):
        X = int(data[index])
        Y = int(data[index + 1])
        Z = int(data[index + 2])
        index += 3
        
        total_estudiantes = X * Y
        if 2 * Z > total_estudiantes:
            resultados.append("YES")
        else:
            resultados.append("NO")
    
    for res in resultados:
        print(res)

if __name__ == "__main__":
    main()