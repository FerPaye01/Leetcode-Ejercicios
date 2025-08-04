import sys

def contar_substrings_distintos(S):
    """Cuenta el número de substrings distintos en S usando Suffix Automaton."""
    n = len(S)
    if n == 0:
        return 0
    
    # Preparamos estructuras con tamaño suficiente (2*n es el máximo teórico de estados)
    max_states = 2 * n + 10
    # Enlace de sufijo para cada estado
    link = [-1] * max_states
    # Longitud máxima del estado
    length = [0] * max_states
    # Transiciones: listas de 26 caracteres (a-z), inicializadas en -1 (sin transición)
    next_state = [[-1] * 26 for _ in range(max_states)]
    
    # Inicialización del automata
    size = 1  # Contador de estados (el estado 0 ya existe)
    last = 0  # Último estado creado
    link[0] = -1  # El estado inicial no tiene enlace
    
    # Construcción del automata carácter por carácter
    for c in S:
        # Convertir carácter a índice (0-25)
        c_idx = ord(c) - ord('a')
        # Crear nuevo estado para el carácter actual
        cur = size
        size += 1
        # La longitud del nuevo estado es la longitud del último + 1
        length[cur] = length[last] + 1
        
        # Paso 1: Seguir enlaces de sufijo y agregar transiciones
        p = last
        # Avanzar por los enlaces de sufijo mientras no haya transición para c
        while p != -1 and next_state[p][c_idx] == -1:
            next_state[p][c_idx] = cur  # Crear transición al nuevo estado
            p = link[p]  # Retroceder al siguiente sufijo
        
        # Paso 2: Manejar los casos después de agregar el carácter
        if p == -1:
            # Caso base: llegamos al estado inicial sin encontrar conflicto
            link[cur] = 0
        else:
            # Encontramos un estado q que ya tiene transición para c
            q = next_state[p][c_idx]
            if length[p] + 1 == length[q]:
                # q está en el punto correcto: heredamos su enlace
                link[cur] = q
            else:
                # Clonar estado q (split state)
                clone = size
                size += 1
                # Copiar propiedades de q
                length[clone] = length[p] + 1
                # Copiar todas las transiciones de q
                next_state[clone] = next_state[q][:]
                link[clone] = link[q]
                
                # Actualizar transiciones de p y ancestros
                while p != -1 and next_state[p][c_idx] == q:
                    next_state[p][c_idx] = clone
                    p = link[p]
                
                # Actualizar enlaces de q y cur
                link[q] = clone
                link[cur] = clone
        # Actualizar último estado al nuevo estado actual
        last = cur
    
    # Calcular total de substrings distintos sumando contribuciones de cada estado
    total_distinct = 0
    for i in range(1, size):
        total_distinct += length[i] - length[link[i]]
    
    return total_distinct

def main():
    """Función principal para manejar entrada y pruebas."""
    if sys.stdin.isatty():
        # Modo de prueba local: ejecutar casos de prueba predefinidos
        test_cases = [
            ("abcbcba", 21),
            ("mississippi", 53),
            ("ababacaca", 33),
            ("aaaaa", 5),
            ("", 0),
            ("a", 1),
            ("ab", 3),
            ("abc", 6),
            ("ababa", 9)
        ]
        for s, esperado in test_cases:
            resultado = contar_substrings_distintos(s)
            print(f"Entrada: '{s}'")
            print(f"Esperado: {esperado}, Resultado: {resultado}")
            print(f"Estado: {'CORRECTO' if resultado == esperado else 'ERROR'}")
            print()
    else:
        # Leer datos de entrada estándar
        S = sys.stdin.readline().strip()
        resultado = contar_substrings_distintos(S)
        print(resultado)

if __name__ == '__main__':
    main()