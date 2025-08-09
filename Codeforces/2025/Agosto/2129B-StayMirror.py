"""
import sys
 
def resolver_caso():
    try:
        # Lee el tamaño de la permutación.
        linea_n = sys.stdin.readline()
        if not linea_n: return
        n = int(linea_n)
 
        # Lee la permutación p.
        p = list(map(int, sys.stdin.readline().split()))
    except (IOError, ValueError):
        # Maneja el caso de fin de archivo o entrada inválida.
        return
 
    # --- Lógica Principal ---
 
    # 1. Calcular las inversiones base en la permutación original p.
    #    Esta es nuestra puntuación inicial si no "espejeamos" ningún elemento.
    #    Complejidad: O(n^2)
    inversiones_base = 0
    for i in range(n):
        for j in range(i + 1, n):
            if p[i] > p[j]:
                inversiones_base += 1
 
    # 2. Para cada elemento p[i], calculamos el efecto de "espejearlo".
    #    La decisión para cada elemento resulta ser independiente del resto,
    #    gracias a que los términos de interacción se cancelan en la suma total.
    delta_inversiones = 0
    for i in range(n):
        valor_actual = p[i]
 
        # Contar cuántos elementos a la derecha son mayores que p[i].
        # (contribución de p[i] a las no-inversiones con el sufijo)
        despues_mayor = 0
        for j in range(i + 1, n):
            if p[j] > valor_actual:
                despues_mayor += 1
 
        # Contar cuántos elementos a la izquierda son mayores que p[i].
        # (contribución de p[i] a las inversiones con el prefijo)
        antes_mayor = 0
        for j in range(i):
            if p[j] > valor_actual:
                antes_mayor += 1
        
        # K_i representa el cambio neto en las inversiones si decidimos
        # espejear el elemento p[i].
        k_i = despues_mayor - antes_mayor
 
        # Para minimizar el total de inversiones, solo aplicamos el cambio
        # si este es negativo (es decir, si reduce el número de inversiones).
        if k_i < 0:
            delta_inversiones += k_i
 
    # El resultado final es la suma de las inversiones base más todos los
    # cambios negativos que decidimos aplicar.
    resultado_final = inversiones_base + delta_inversiones
    print(resultado_final)
 
 
def main():
    # La estructura `sys.stdin.read().split()` que mencionaste no es ideal para
    # problemas con múltiples casos de prueba de longitud variable.
    # El enfoque estándar y más robusto, que se utiliza aquí, es leer el número
    # de casos y luego procesar cada uno secuencialmente.
    try:
        num_casos = int(sys.stdin.readline())
        for _ in range(num_casos):
            resolver_caso()
    except (IOError, ValueError):
        # Termina si no hay más entrada o la entrada es inválida.
        return
 
if __name__ == "__main__":
    main()"""


import sys

def resolver_permutacion(p):
    """
    Recibe una lista p (permutación) y devuelve el número mínimo de inversiones
    tras aplicar las decisiones locales de "espejado" cuando reducen el total.
    La lógica es exactamente la del algoritmo original que compartiste, pero
    encapsulada para recibir directamente la permutación.
    """
    n = len(p)

    # 1) Inversiones base en p (conteo de pares (i<j) con p[i] > p[j])
    inversiones_base = 0
    for i in range(n):
        for j in range(i + 1, n):
            if p[i] > p[j]:
                inversiones_base += 1

    # 2) Para cada posición i calculamos K_i = (# a la derecha mayores que p[i])
    #    - (# a la izquierda mayores que p[i]).
    #    Si K_i < 0, lo aplicamos (reduce el total).
    delta_inversiones = 0
    for i in range(n):
        valor = p[i]

        # contar elementos a la derecha mayores que valor
        despues_mayor = 0
        for j in range(i + 1, n):
            if p[j] > valor:
                despues_mayor += 1

        # contar elementos a la izquierda mayores que valor
        antes_mayor = 0
        for j in range(i):
            if p[j] > valor:
                antes_mayor += 1

        k_i = despues_mayor - antes_mayor
        if k_i < 0:
            delta_inversiones += k_i

    return inversiones_base + delta_inversiones


def main():
    """
    Programa principal orientado a imprimir resultados por testcase. Aquí construimos
    explícitamente la entrada (como en tu ejemplo) y procesamos cada caso, mostrando
    el resultado en una línea por caso (idéntico al formato de OutputCopy).
    """

    # === Definición explícita de los test cases (según tu ejemplo) ===
    test_cases = [
        [2, 1],                 # caso 1
        [2, 1, 3],              # caso 2
        [4, 3, 2, 1],          # caso 3
        [2, 3, 1, 5, 4],       # caso 4
        [2, 3, 4, 1, 5, 6]     # caso 5
    ]

    # Si prefieres construir desde una representación tipo "stdin" (simulada)
    # se podría parsear, pero con la lista anterior es directo.
    resultados = []
    for p in test_cases:
        resultado = resolver_permutacion(p)
        resultados.append(str(resultado))

    # Imprimimos un resultado por línea (formato requerido).
    print("\n".join(resultados))


if __name__ == "__main__":
    main()
