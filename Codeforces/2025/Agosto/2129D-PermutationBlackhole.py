#!/usr/bin/env python3  # Shebang: usar el intérprete de Python 3 disponible en el entorno
# Solución Python optimizada (PyPy-friendly) para "Permutation Blackhole".  # Descripción breve del módulo
# Variables en español; DP por intervalos con representacion plana para matrices.  # Resumen de estilo

import sys  # Importa el módulo sys para acceder a stdin y funciones del intérprete
import math  # Importa el módulo math para funciones matemáticas (log2, ceil)

MOD = 998244353  # Constante: módulo primo usado para todas las operaciones aritméticas

def precompute_factorials(n_max):  # Función que precomputa factorizaciones hasta n_max
    fact = [1] * (n_max + 1)  # Inicializa arreglo de factoriales con 1s de tamaño n_max+1
    invfact = [1] * (n_max + 1)  # Inicializa arreglo de factoriales inversos con 1s
    for i in range(1, n_max + 1):  # Itera i desde 1 hasta n_max inclusive
        fact[i] = fact[i-1] * i % MOD  # Calcula fact[i] = i! mod MOD usando relación fact[i]=fact[i-1]*i
    invfact[n_max] = pow(fact[n_max], MOD-2, MOD)  # Calcula invfact[n_max] = (fact[n_max])^{-1} mod MOD por exponenciación modular
    for i in range(n_max, 0, -1):  # Itera a la inversa para completar invfact (i decrece)
        invfact[i-1] = invfact[i] * i % MOD  # Usa invfact[i-1] = invfact[i] * i mod MOD para eficiencia
    return fact, invfact  # Devuelve tupla (fact, invfact) para combinatoria O(1)

def comb(n, k, fact, invfact):  # Función combinatoria C(n,k) modular con precomputados
    if k < 0 or k > n:  # Si k fuera inválido
        return 0  # C(n,k) = 0 para k fuera de rango
    return fact[n] * invfact[k] % MOD * invfact[n-k] % MOD  # Calcula C(n,k) = n!/(k!(n-k)!) mod MOD

def procesar_caso(cadena_s, fact, invfact):  # Función principal que resuelve un caso dado s[]
    n = len(cadena_s)  # Tamaño del problema n derivado de la longitud de la secuencia s
    LOG = max(7, math.ceil(math.log2(max(1, n))) + 5)  # Cota dinámica LOG = ceil(log2(n))+5, con mínimo 7 (margen conservador)

    for v in cadena_s:  # Recorre todos los elementos de s
        if v >= LOG:  # Si algún valor s[i] excede o iguala la cota LOG
            return 0  # Entonces no hay permutaciones válidas (rechazo temprano por cota teórica/práctica)

    dp = [[None] * (n + 2) for _ in range(n + 2)]  # Estructura dp 2D (matriz) para almacenar resultados por intervalo (1..n)

    def dp_vacio():  # Constructor auxiliar para el DP de intervalo vacío
        return (1, 1, [1])  # Representa matriz 1x1 con único elemento 1 (estado base)

    for tam in range(1, n + 1):  # Itera tamaños de intervalo tam desde 1 hasta n (bottom-up)
        for l in range(1, n - tam + 2):  # Itera posiciones de inicio l posibles para el intervalo
            r = l + tam - 1  # Calcula el extremo derecho r del intervalo actual

            if l == 1:  # Si el intervalo toca el borde izquierdo del arreglo global
                max_x = 0  # No hay contribución hacia la izquierda externa
            else:
                s_ext_izq = cadena_s[l - 2]  # Toma el valor s[l-1] (índice externo izquierdo en 1-based)
                max_x = (s_ext_izq if s_ext_izq != -1 else (LOG - 1))  # Si está fijado, usarlo; si -1 usar LOG-1 como cota

            if r == n:  # Si el intervalo toca el borde derecho del arreglo global
                max_y = 0  # No hay contribución hacia la derecha externa
            else:
                s_ext_der = cadena_s[r]  # Toma el valor s[r+1] en notación 1-based
                max_y = (s_ext_der if s_ext_der != -1 else (LOG - 1))  # Similar a la izquierda: valor fijo o cota LOG-1

            if max_x < 0: max_x = 0  # Sanitiza por si acaso (garantía de no-negatividad)
            if max_y < 0: max_y = 0  # Igual para max_y

            rows = max_x + 1  # Número de filas de la matriz de estados = max_x + 1
            cols = max_y + 1  # Número de columnas de la matriz de estados = max_y + 1
            flat = [0] * (rows * cols)  # Representación plana (1D) de la matriz rows x cols inicializada a ceros

            for k in range(l, r + 1):  # Recorre posibles pivotes k dentro del intervalo [l,r]
                if l == 1 and r == n:  # Caso especial: intervalo abarca todo el arreglo
                    tagl = 0; tagr = 0  # Ninguna frontera externa existe, no se incrementa ninguna
                elif l == 1:  # Si el intervalo toca la izquierda global pero no la derecha
                    tagl = 0; tagr = 1  # Pintar k incrementará la frontera derecha del intervalo
                elif r == n:  # Si el intervalo toca la derecha global pero no la izquierda
                    tagl = 1; tagr = 0  # Pintar k incrementará la frontera izquierda del intervalo
                else:
                    if abs((l - 1) - k) <= abs(k - (r + 1)):  # Compara distancias simétricas a las celdas externas
                        tagl = 1; tagr = 0  # Si la frontera izquierda está más cerca (o empate) incrementa izquierda
                    else:
                        tagl = 0; tagr = 1  # Si la frontera derecha está más cerca incrementa derecha

                left = dp[l][k-1] if k-1 >= l else dp_vacio()  # Subresultado izquierdo: dp[l][k-1] o base si vacío
                right = dp[k+1][r] if k+1 <= r else dp_vacio()  # Subresultado derecho: dp[k+1][r] o base si vacío

                lx, ly, lflat = left  # Desempaqueta la matriz izquierda: filas lx, columnas ly, arreglo plano lflat
                rx, ry, rflat = right  # Desempaqueta la matriz derecha: filas rx, columnas ry, arreglo plano rflat

                max_x_izq = lx - 1  # Contribución máxima que puede aportar la izquierda (filas-1)
                max_y_izq = ly - 1  # Columnas-1 de la izquierda (máximo índice j)
                max_x_der = rx - 1  # Contribución máxima que puede aportar la derecha (filas-1)
                max_y_der = ry - 1  # Columnas-1 de la derecha

                sk = cadena_s[k - 1]  # Valor s[k] para el pivote k, puede ser -1 (no fijado) o >=0 (fijado)
                coef = comb(r - l, k - l, fact, invfact)  # Coeficiente combinatorio C(r-l, k-l) para interleaving de órdenes
                mul_local = coef % MOD  # Versión modular del coeficiente para operaciones repetidas
                MOD_local = MOD  # Enlace local de la constante MOD para velocidad en bucles calientes

                sumRow_izq = [0] * (max_x_izq + 1)  # Inicializa array para sumas por cada fila de la izquierda
                for a in range(max_x_izq + 1):  # Para cada fila a de la izquierda
                    s_acc = 0  # Acumulador temporal para la suma de la fila
                    base = a * ly  # Índice base en lflat para la fila a
                    for b in range(ly):  # Recorre todas las columnas b de la fila a
                        s_acc += lflat[base + b]  # Suma los valores dp_izq[a][b]
                    sumRow_izq[a] = s_acc % MOD_local  # Guarda la suma modular en sumRow_izq[a]

                sumCol_der = [0] * (max_y_der + 1)  # Inicializa array para sumas por cada columna de la derecha
                for d in range(max_y_der + 1):  # Para cada columna d de la derecha
                    s_acc = 0  # Acumulador temporal para la suma de la columna
                    base = d  # Offset inicial para acceder a rflat en columna d (stride = ry)
                    for c in range(rx):  # Recorre todas las filas c de la derecha
                        s_acc += rflat[c * ry + d]  # Suma los valores dp_der[c][d] mediante index plano
                    sumCol_der[d] = s_acc % MOD_local  # Guarda la suma modular en sumCol_der[d]

                if sk == -1:  # Si s[k] no está fijado (libre)
                    for a in range(max_x_izq + 1):  # Para cada contribución posible a la izquierda a
                        dest_i = a + tagl  # Índice de fila destino en la matriz resultante (desplazado por tagl)
                        if dest_i > max_x:  # Si sale del rango permitido por max_x, saltar
                            continue
                        pref = (sumRow_izq[a] * mul_local) % MOD_local  # Prefactor que combina suma izquierda y coef
                        base_dest_i = dest_i * cols  # Base plana para acceder a la fila dest_i en el arreglo flat
                        for d in range(max_y_der + 1):  # Para cada contribución posible a la derecha d
                            dest_j = d + tagr  # Índice de columna destino en la matriz resultante
                            if dest_j > max_y:  # Si columna destino fuera de rango, saltar
                                continue
                            idx = base_dest_i + dest_j  # Índice plano en flat para (dest_i, dest_j)
                            flat[idx] = (flat[idx] + pref * sumCol_der[d]) % MOD_local  # Acumula la contribución modular en flat
                else:  # Si s[k] está fijado a un valor concreto
                    for a in range(max_x_izq + 1):  # Para cada posible contribución a la izquierda a
                        dest_i = a + tagl  # Calcula la fila destino correspondiente
                        if dest_i > max_x:  # Si fuera de rango en la matriz destino, saltar
                            continue
                        base_dest_i = dest_i * cols  # Base plana para la fila destino en flat
                        base_lrow = a * ly  # Base plana para la fila a en lflat
                        for d in range(max_y_der + 1):  # Para cada posible contribución a la derecha d
                            dest_j = d + tagr  # Columna destino en la matriz resultado
                            if dest_j > max_y:  # Si fuera de rango en columnas destino, saltar
                                continue
                            b_low = sk - max_x_der  # Límite inferior del sumatorio b tal que kk = sk - b esté en rango
                            if b_low < 0:
                                b_low = 0  # Ajuste de frontera inferior a 0 si era negativo
                            b_high = sk  # Límite superior natural del sumatorio b
                            if b_high > max_y_izq:
                                b_high = max_y_izq  # Ajuste de frontera superior al máximo j disponible en izquierda
                            if b_low > b_high:  # Si intervalo de b vacío, no hay contribución
                                continue
                            s_acc = 0  # Acumulador para la suma interna que calcula la convolución corta
                            for b in range(b_low, b_high + 1):  # Itera los b permitidos por la restricción j+kk=sk
                                kk = sk - b  # Correspondiente contribución kk de la parte derecha
                                s_acc += lflat[base_lrow + b] * rflat[kk * ry + d]  # Producto y suma sin módulo intermedio
                            if s_acc:  # Si la suma interna no es cero
                                idx = base_dest_i + dest_j  # Índice plano destino en flat
                                flat[idx] = (flat[idx] + mul_local * (s_acc % MOD_local)) % MOD_local  # Acumula modulado en flat

            dp[l][r] = (rows, cols, flat)  # Almacena la matriz plana resultante para el intervalo [l,r] en dp

    final = dp[1][n]  # Recupera la matriz final correspondiente al intervalo completo [1,n]
    if final is None:  # Si por alguna razón no se llenó (caso borde)
        return 0  # No hay soluciones válidas
    rowsf, colsf, flatf = final  # Desempaqueta la matriz final
    return flatf[0] % MOD  # Devuelve el estado [0,0] (sin contribuciones externas) módulo MOD

def main():  # Función principal que gestiona E/S y llamadas a la resolución por caso
    if sys.stdin.isatty():  # Si stdin es interactivo (ejecución local), usar entrada interna de prueba
        raw_input = """9
3
-1 -1 1
3
-1 -1 -1
4
-1 2 -1 0
4
-1 0 1 -1
5
-1 3 -1 0 -1
5
4 4 4 4 4
5
1 0 1 2 0
6
-1 1 -1 -1 3 0
13
-1 -1 -1 -1 -1 -1 2 -1 -1 -1 -1 -1 -1
"""  # Ejemplo de entrada para pruebas locales
        data = raw_input.strip().split()  # Tokeniza la entrada de prueba en una lista de strings
    else:
        data = sys.stdin.read().strip().split()  # Lee y tokeniza la entrada estándar en modo competitivo

    if not data:  # Si no hay tokens -> no hay entrada
        return  # Finaliza ejecución sin salida
    it = iter(data)  # Crea iterador sobre los tokens de entrada
    t = int(next(it))  # Lee el número de casos t desde el iterador
    casos = []  # Lista que almacenará tuplas (n, s)
    max_n = 0  # Variable para rastrear el máximo n entre casos (para precomputar factoriales)

    for _ in range(t):  # Recorre cada caso de prueba
        n = int(next(it))  # Lee el tamaño n del caso actual
        s = [int(next(it)) for _ in range(n)]  # Lee los n valores de la secuencia s como enteros
        casos.append((n, s))  # Almacena el par (n, s) en la lista de casos
        if n > max_n:  # Actualiza el máximo n si el actual es mayor
            max_n = n  # Guarda nueva cota para precomputación de factoriales

    fact, invfact = precompute_factorials(max(1, max_n))  # Precomputa factoriales e inversos hasta max_n

    out_lines = []  # Lista para almacenar resultados como cadenas
    for (n, s) in casos:  # Para cada caso en la lista de casos
        out_lines.append(str(procesar_caso(s, fact, invfact)))  # Ejecuta la resolución y añade resultado stringificado
    sys.stdout.write("\n".join(out_lines) + "\n")  # Imprime todos los resultados, uno por línea, y termina con salto

if __name__ == "__main__":  # Estándar guard: ejecuta main solo si el script es invocado directamente
    main()  # Llamada a la función principal para iniciar el procesamiento
