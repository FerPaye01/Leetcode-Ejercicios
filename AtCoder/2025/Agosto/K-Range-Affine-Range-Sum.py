#!/usr/bin/env python3  # Ejecutable: usar el intérprete Python disponible en el entorno
import sys  # Importa el módulo sys para entrada/salida y control del intérprete
sys.setrecursionlimit(1 << 25)  # Aumenta el límite de recursión para seguridad en recursión logarítmica

MOD = 998244353  # Constante modular exigida por el enunciado

def resolver_tokens(tokens):  # Función principal que resuelve la instancia a partir de tokens enteros
    """Resuelve un caso completo a partir de una lista de enteros (tokens)."""  # Docstring breve de la función
    it = iter(tokens)  # Crea un iterador sobre los tokens para consumo secuencial
    try:
        n = next(it)  # Lee la primera posición: tamaño del arreglo N
    except StopIteration:
        return ""  # Si no hay tokens, devuelve cadena vacía (nada que resolver)
    q = next(it)  # Lee la segunda posición: número de consultas Q

    # leer arreglo inicial
    a = [next(it) % MOD for _ in range(n)]  # Construye el arreglo inicial módulo MOD

    # tamaño del árbol (potencia de 2)
    n0 = 1 << ((n - 1).bit_length())  # Calcula la mínima potencia de 2 >= n para el segment tree

    # estructuras del árbol (array plano)
    suma = [0] * (2 * n0)  # Array de sumas por nodo (almacena la suma del segmento)
    longitud = [0] * (2 * n0)  # Array con la longitud (número de elementos) de cada nodo
    b_pend = [1] * (2 * n0)   # Pendiente multiplicativa por nodo (identidad = 1)
    c_pend = [0] * (2 * n0)   # Pendiente aditiva por nodo (identidad = 0)

    # inicializar longitudes en hojas
    for i in range(n0):  # Recorre cada hoja potencial del árbol
        longitud[n0 + i] = 1 if i < n else 0  # Asigna 1 si existe elemento en esa hoja, 0 si es relleno
    for i in range(n0 - 1, 0, -1):  # Recorre nodos internos de derecha a izquierda
        longitud[i] = longitud[2 * i] + longitud[2 * i + 1]  # Suma las longitudes de los hijos

    # llenar hojas con el array
    for i in range(n):  # Recorre índices válidos del arreglo original
        suma[n0 + i] = a[i]  # Coloca cada valor en la hoja correspondiente
    for i in range(n0 - 1, 0, -1):  # Construye las sumas internas del árbol
        suma[i] = (suma[2 * i] + suma[2 * i + 1]) % MOD  # Suma modular de los hijos

    # aplicar transformación afín (b,c) al nodo 'i'
    def aplicar_nodo(i, b, c):  # Aplica f(x)=b*x + c a todo el segmento representado por el nodo i
        suma[i] = (b * suma[i] + c * longitud[i]) % MOD  # Actualiza la suma del nodo tras la transformación
        b_pend[i] = (b * b_pend[i]) % MOD  # Compone el factor multiplicativo pendiente en el nodo
        c_pend[i] = (b * c_pend[i] + c) % MOD  # Compone el término aditivo pendiente en el nodo

    # propagar pendientes del nodo i hacia sus hijos
    def push(i):  # Propaga las pendientes almacenadas en el nodo i hacia sus hijos inmediatos
        bi = b_pend[i]  # Extrae la pendiente multiplicativa local
        ci = c_pend[i]  # Extrae la pendiente aditiva local
        if bi == 1 and ci == 0:  # Si la pendiente es la identidad, no hay nada que propagar
            return  # Sale sin modificar nada
        aplicar_nodo(2 * i, bi, ci)  # Aplica la pendiente al hijo izquierdo
        aplicar_nodo(2 * i + 1, bi, ci)  # Aplica la pendiente al hijo derecho
        b_pend[i] = 1  # Resetea la pendiente multiplicativa del nodo a la identidad
        c_pend[i] = 0  # Resetea la pendiente aditiva del nodo a la identidad

    # actualizar rango [l, r) con transformacion (b, c)
    def actualizar_rango(l, r, b, c, i=1, nl=0, nr=None):  # Función recursiva para aplicar la transformación en [l,r)
        if nr is None:
            nr = n0  # Inicializa el límite derecho del segmento en la raíz si no se proporcionó
        if r <= nl or nr <= l:  # Caso de no solapamiento entre [l,r) y [nl,nr)
            return  # No hacer nada si no se solapan
        if l <= nl and nr <= r:  # Caso de cobertura total: el nodo está completamente dentro de [l,r)
            aplicar_nodo(i, b, c)  # Aplica la transformación al nodo y acumula la pendiente
            return  # Termina la recursión en esta rama
        push(i)  # Antes de bajar, propaga pendientes pendientes en el nodo i
        mid = (nl + nr) >> 1  # Calcula el punto medio del segmento [nl,nr)
        if l < mid:
            actualizar_rango(l, r, b, c, 2 * i, nl, mid)  # Recurre al hijo izquierdo si hay solapamiento
        if r > mid:
            actualizar_rango(l, r, b, c, 2 * i + 1, mid, nr)  # Recurre al hijo derecho si hay solapamiento
        suma[i] = (suma[2 * i] + suma[2 * i + 1]) % MOD  # Actualiza la suma del nodo tras actualizar hijos

    # consultar suma en rango [l, r)
    def consultar_rango(l, r, i=1, nl=0, nr=None):  # Consulta recursiva de la suma en [l,r)
        if nr is None:
            nr = n0  # Inicializa el límite derecho del segmento en la raíz si no se proporcionó
        if r <= nl or nr <= l:  # Si no hay solapamiento
            return 0  # Devuelve 0 neutro para la suma
        if l <= nl and nr <= r:  # Si el nodo está completamente dentro del rango de consulta
            return suma[i]  # Retorna la suma almacenada en el nodo
        push(i)  # Asegura que las pendientes se apliquen antes de consultar hijos
        mid = (nl + nr) >> 1  # Punto medio del segmento
        res = 0  # Inicializa acumulador de resultado
        if l < mid:
            res += consultar_rango(l, r, 2 * i, nl, mid)  # Consulta hijo izquierdo si corresponde
        if r > mid:
            res += consultar_rango(l, r, 2 * i + 1, mid, nr)  # Consulta hijo derecho si corresponde
        return res % MOD  # Retorna el resultado modularizado

    # procesar queries
    out_lines = []  # Lista para acumular las líneas de salida para consultas tipo 1
    for _ in range(q):  # Recorre todas las Q consultas
        t = next(it)  # Lee el tipo de consulta (0: update, 1: query)
        if t == 0:
            l = next(it)  # Límite izquierdo de la actualización (inclusive)
            r = next(it)  # Límite derecho de la actualización (exclusive)
            b = next(it) % MOD  # Coeficiente multiplicativo b modulo MOD
            c = next(it) % MOD  # Término aditivo c modulo MOD
            actualizar_rango(l, r, b, c)  # Ejecuta la actualización afín en el rango
        else:
            l = next(it)  # Límite izquierdo de la consulta (inclusive)
            r = next(it)  # Límite derecho de la consulta (exclusive)
            ans = consultar_rango(l, r)  # Obtiene la suma en el rango solicitado
            out_lines.append(str(ans % MOD))  # Añade la respuesta formateada a la salida

    return "\n".join(out_lines)  # Devuelve todas las respuestas unidas por saltos de línea


def main():  # Función principal que gestiona modo local interactivo y modo juez
    if sys.stdin.isatty():  # Si la entrada estándar es interactiva, activamos casos de prueba locales
        casos_prueba = [  # Lista de casos de prueba locales predefinidos
            [5, 7,
             1, 2, 3, 4, 5,
             1, 0, 5,
             0, 2, 4, 100, 101,
             1, 0, 3,
             0, 1, 3, 102, 103,
             1, 2, 5,
             0, 2, 5, 104, 105,
             1, 0, 5],
            [3, 4,
             0, 0, 0,
             1, 0, 3,
             0, 0, 2, 2, 3,
             1, 0, 2],
        ]
        for idx, tokens in enumerate(casos_prueba, 1):  # Itera y ejecuta cada caso local
            print(f"--- Caso de prueba local #{idx} ---")  # Muestra identificación del caso local
            salida = resolver_tokens(tokens)  # Resuelve el caso con la función central
            if salida:
                print(salida)  # Imprime la salida si existe
            else:
                print("(sin salida)")  # Indica si no hubo salida producida
            print()  # Línea en blanco separadora entre casos
    else:
        data = list(map(int, sys.stdin.buffer.read().split()))  # Lee todo stdin y lo tokeniza a enteros
        if not data:
            return  # Si no hay datos, salir sin imprimir
        salida = resolver_tokens(data)  # Resolver la única instancia proveniente del juez
        if salida:
            sys.stdout.write(salida + "\n")  # Escribe la salida final con salto de línea terminal

if __name__ == "__main__":
    main()  # Punto de entrada: ejecuta main si el fichero se ejecuta directamente
