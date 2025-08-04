from collections import defaultdict
from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        izquierda = 0  # Puntero izquierdo de la ventana
        max_frutas = 0  # Almacena el máximo número de frutas recolectadas
        conteo_frutas = defaultdict(int)  # Diccionario para contar tipos de frutas
        
        # Iterar con el puntero derecho sobre todos los árboles
        for derecha in range(len(fruits)):
            fruta_actual = fruits[derecha]  # Fruta del árbol actual
            conteo_frutas[fruta_actual] += 1  # Aumentar conteo de esta fruta
            
            # Si hay más de 2 tipos de frutas, contraer la ventana
            while len(conteo_frutas) > 2:
                fruta_izq = fruits[izquierda]  # Fruta en el extremo izquierdo
                conteo_frutas[fruta_izq] -= 1  # Reducir su conteo
                # Eliminar fruta si su conteo llega a cero
                if conteo_frutas[fruta_izq] == 0:
                    del conteo_frutas[fruta_izq]
                izquierda += 1  # Mover puntero izquierdo
            
            # Actualizar el máximo (tamaño actual de la ventana)
            max_frutas = max(max_frutas, derecha - izquierda + 1)
        
        return max_frutas  # Devolver el máximo encontrado

def main():
    sol = Solution()
    # Casos de prueba: (lista de frutas, resultado esperado)
    test_cases = [
        ([1, 2, 1], 3),
        ([0, 1, 2, 2], 3),
        ([1, 2, 3, 2, 2], 4),
        ([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4], 5),
        ([1, 2, 3, 2, 1], 4),
        ([1, 1, 1, 1, 1], 5),
        ([1, 2, 3, 4, 5], 2)
    ]

    for i, (fruits, expected) in enumerate(test_cases):
        result = sol.totalFruit(fruits)
        # Verificar e imprimir resultado con iconos
        print(f"Test case {i + 1}: Fruits = {fruits} -> Resultado = {result} (Esperado: {expected}) {'✅' if result == expected else '❌'}")

if __name__ == "__main__":
    main()