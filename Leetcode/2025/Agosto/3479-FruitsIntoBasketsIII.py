from typing import List

class SegmentTree:
    def __init__(self, data):
        """
        Inicializa el árbol de segmentos para realizar consultas de mínimo en un rango.
        - data: lista de enteros, aquí se usa una lista de índices para organizar las canastas.
        Construye un árbol binario completo, rellenando con valores altos para posiciones vacías.
        """
        self.n = len(data)
        self.size = 1
        while self.size < self.n:  # Tamaño mínimo potencia de 2 >= n
            self.size *= 2
        # Inicializa el árbol con pares (valor, índice), valor muy grande para vacíos
        self.tree = [(10**18, -1)] * (2 * self.size)
        # Inserta los datos originales en las hojas del árbol
        for i in range(self.n):
            self.tree[self.size + i] = (data[i], i)
        # Completa las hojas restantes con valores grandes (sin datos)
        for i in range(self.n, self.size):
            self.tree[self.size + i] = (10**18, i)
        # Construye el árbol desde las hojas hacia la raíz combinando pares
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.combine(self.tree[2*i], self.tree[2*i+1])
    
    def combine(self, a, b):
        """
        Combina dos pares (valor, índice) devolviendo el de menor valor.
        En caso de empate, devuelve 'b'.
        """
        if a[0] < b[0]:
            return a
        else:
            return b
            
    def update(self, index, value):
        """
        Actualiza el valor en la posición 'index' del arreglo base con 'value'
        y actualiza los nodos del árbol correspondientes hacia la raíz.
        """
        i = self.size + index
        self.tree[i] = (value, index)
        i //= 2
        while i:
            self.tree[i] = self.combine(self.tree[2*i], self.tree[2*i+1])
            i //= 2

    def query(self, l, r):
        """
        Consulta el mínimo valor y su índice en el rango [l, r].
        Utiliza la técnica de recorrido de segmento en el árbol.
        """
        l += self.size
        r += self.size
        res = (10**18, -1)
        while l <= r:
            if l % 2 == 1:
                res = self.combine(res, self.tree[l])
                l += 1
            if r % 2 == 0:
                res = self.combine(res, self.tree[r])
                r -= 1
            l //= 2
            r //= 2
        return res

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        """
        Dada una lista de frutas y canastas con capacidades, determina cuántas frutas
        no se pueden colocar en ninguna canasta que tenga capacidad suficiente.
        Estrategia:
        1. Ordena las canastas por capacidad manteniendo índices originales.
        2. Usa un Segment Tree para encontrar la canasta disponible con el índice mínimo
           (para mantener la canasta menos usada) en el rango adecuado.
        3. Para cada fruta, busca la primera canasta que pueda contenerla (binaria).
        4. Consulta el Segment Tree para encontrar la canasta disponible con índice mínimo.
        5. Si no hay canasta disponible, incrementa el conteo de frutas no colocadas.
        """
        n = len(fruits)
        # Empareja capacidad con índice original para ordenar sin perder referencia
        canastas = [(baskets[i], i) for i in range(n)]
        canastas.sort(key=lambda x: (x[0], x[1]))
        capacidades = [c[0] for c in canastas]
        indices_originales = [c[1] for c in canastas]
        
        seg_tree = SegmentTree(indices_originales)
        no_colocadas = 0
        
        for fruta in fruits:
            # Búsqueda binaria para encontrar la primera canasta con capacidad >= fruta
            lo, hi = 0, n-1
            pos_inicio = n
            while lo <= hi:
                mid = (lo + hi) // 2
                if capacidades[mid] >= fruta:
                    pos_inicio = mid
                    hi = mid - 1
                else:
                    lo = mid + 1
            
            if pos_inicio == n:
                # No hay canasta con capacidad suficiente
                no_colocadas += 1
            else:
                # Consulta Segment Tree para obtener canasta con índice mínimo disponible
                min_val, min_pos = seg_tree.query(pos_inicio, n-1)
                if min_val == 10**18:
                    # No quedan canastas disponibles con esa capacidad
                    no_colocadas += 1
                else:
                    # Marca la canasta como usada actualizando con valor muy alto
                    seg_tree.update(min_pos, 10**18)
        
        return no_colocadas

def main():
    """
    Función principal que prueba varios casos de ejemplo para la función
    numOfUnplacedFruits, imprimiendo resultados con validación automática.
    """
    sol = Solution()
    # Casos de prueba: ((lista de frutas, lista de canastas), resultado esperado)
    test_cases = [
        (([4, 2, 5], [3, 5, 4]), 1),    # Ejemplo 1
        (([3, 6, 1], [6, 4, 7]), 0),     # Ejemplo 2
        (([10], [5]), 1),                # Fruta grande no cabe
        (([1, 1], [1, 1]), 0),          # Todas las frutas caben exactamente
        (([1, 2], [2, 1]), 1),          # Segunda fruta no cabe en la segunda canasta
        (([5, 3, 2], [2, 5, 4]), 0),    # Todas las frutas colocadas
        (([7, 8, 9], [5, 5, 5]), 3),    # Ninguna fruta cabe
        (([5, 4, 3, 2], [6, 5, 4, 3]), 0) # Todas colocadas en orden inverso
    ]

    for i, ((fruits, baskets), expected) in enumerate(test_cases):
        result = sol.numOfUnplacedFruits(fruits, baskets)
        # Verificar e imprimir resultado con iconos
        print(f"Test case {i + 1}: Fruits = {fruits}, Baskets = {baskets} -> Resultado = {result} (Esperado: {expected}) {'✅' if result == expected else '❌'}")

if __name__ == "__main__":
    main()