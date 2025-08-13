"""
Problem Statement
AtCoDeer the deer found two positive integers, a and b. Determine whether 
the product of a and b is even or odd.

Constraints
- 1 ≤ a, b ≤ 10000
- a and b are integers.

Input
Input is given from Standard Input in the following format:
a  b

Output
If the product is odd, print Odd; if it is even, print Even.

Sample Input 1
3 4

Sample Output 1
Even

As 3 × 4 = 12 is even, print Even.

Sample Input 2
1 21

Sample Output 2
Odd

As 1 × 21 = 21 is odd, print Odd.
"""
import sys  # Importa el módulo estándar 'sys' para acceder a stdin, stdout y funciones del sistema.

def procesar_caso(tokens):  # Define una función llamada 'procesar_caso' con parámetro 'tokens' (lista de cadenas).
    if len(tokens) < 2:  # Verifica si la longitud de la lista es menor que 2, usando la función 'len()'.
        return  # Devuelve None y termina la ejecución de la función si la condición previa es verdadera.
    entero_a = int(tokens[0])  # Convierte el primer elemento (str) de 'tokens' a entero base 10 usando 'int()'.
    entero_b = int(tokens[1])  # Convierte el segundo elemento (str) de 'tokens' a entero base 10 usando 'int()'.
    if entero_a % 2 == 0 or entero_b % 2 == 0:  # Aplica el operador módulo '%' para comprobar si alguno es par.
        print("Even")  # Imprime la cadena literal "Even" en stdout seguida de salto de línea.
    else:  # Bloque alternativo ejecutado si ninguno de los operandos es par (ambos impares).
        print("Odd")  # Imprime la cadena literal "Odd" en stdout seguida de salto de línea.

def main():  # Define la función 'main', punto de entrada principal del programa.
    if sys.stdin.isatty():  # Verifica si stdin está conectado a un terminal interactivo usando 'isatty()'.
        casos_prueba = [  # Declara una lista de listas con casos de prueba predefinidos (cada sublista = par de números).
            ["3", "4"],   # Lista de dos cadenas "3" y "4" (caso de producto par: 3*4=12).
            ["1", "21"],  # Lista de cadenas para producto impar: 1*21=21.
            ["2", "3"],   # Producto par: 2*3=6.
            ["5", "5"],   # Producto impar: 5*5=25.
            ["10000", "10000"], # Producto par: 10000*10000.
            ["9999", "10000"]   # Producto par: 9999*10000.
        ]  # Cierre de la lista 'casos_prueba'.
        for tokens in casos_prueba:  # Itera sobre cada sublista en 'casos_prueba' asignándola a 'tokens'.
            print(f"--- Caso de prueba: {tokens} ---")  # Usa f-string para interpolar la lista 'tokens' en un formato fijo.
            procesar_caso(tokens)  # Llama a la función 'procesar_caso' pasando la lista actual como argumento.
            print()  # Imprime una línea en blanco (salto de línea) para separar salidas.
    else:  # Rama ejecutada cuando stdin no proviene de un terminal (ej. redirección o pipe).
        data = sys.stdin.read().split()  # Lee todo stdin como cadena y lo divide por espacios en una lista de tokens.
        procesar_caso(data)  # Llama a 'procesar_caso' con los datos obtenidos desde stdin.

if __name__ == "__main__":  # Comprueba si el script se ejecuta como programa principal y no como módulo importado.
    main()  # Llama a la función 'main' para iniciar la ejecución del programa.
