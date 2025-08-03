import bisect

class Solution:
    def maxTotalFruits(self, fruits: list, startPos: int, k: int) -> int:
        if not fruits:
            return 0
        
        # Extraer posiciones y cantidades de frutas
        pos = [f[0] for f in fruits]
        arr = [f[1] for f in fruits]
        n = len(pos)
        
        # Construir arreglo de sumas de prefijos
        prefix = [0] * n
        prefix[0] = arr[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1] + arr[i]
        
        # Función para calcular la suma de frutas en un intervalo [l, r]
        def suma_intervalo(l, r):
            if r < pos[0] or l > pos[-1]:
                return 0
            left_idx = bisect.bisect_left(pos, l)
            right_idx = bisect.bisect_right(pos, r) - 1
            if left_idx > right_idx:
                return 0
            return prefix[right_idx] - (prefix[left_idx - 1] if left_idx > 0 else 0)
        
        max_frutas = 0
        
        # Caso 1: Moverse solo a la izquierda
        l1 = startPos - k
        r1 = startPos
        s1 = suma_intervalo(l1, r1)
        max_frutas = max(max_frutas, s1)
        
        # Caso 2: Moverse solo a la derecha
        l2 = startPos
        r2 = startPos + k
        s2 = suma_intervalo(l2, r2)
        max_frutas = max(max_frutas, s2)
        
        # Caso 3: Primero izquierda, luego derecha
        # Índice de la última posición <= startPos
        i_left_end = bisect.bisect_right(pos, startPos) - 1
        if i_left_end >= 0:
            # Iterar sobre todas las posiciones a la izquierda de startPos
            for i in range(i_left_end + 1):
                L = pos[i]
                # Calcular el límite derecho basado en los pasos restantes
                R_max = k + 2 * L - startPos
                if R_max < startPos:  # No cubre startPos
                    continue
                # El límite derecho no debe exceder la última posición disponible
                R_bound = min(R_max, pos[-1])
                s3 = suma_intervalo(L, R_bound)
                max_frutas = max(max_frutas, s3)
        
        # Caso 4: Primero derecha, luego izquierda
        i_right_start = bisect.bisect_left(pos, startPos)
        if i_right_start < n:
            # Iterar sobre todas las posiciones a la derecha de startPos
            for j in range(i_right_start, n):
                R = pos[j]
                # Calcular el límite izquierdo basado en los pasos restantes
                L_min = 2 * R - k - startPos
                if L_min > startPos:  # No cubre startPos
                    continue
                # El límite izquierdo no debe ser menor que la primera posición
                L_bound = max(0, L_min)
                s4 = suma_intervalo(L_bound, R)
                max_frutas = max(max_frutas, s4)
        
        return max_frutas

def main():
    sol = Solution()

    test_cases = [
        ([[2,8],[6,3],[8,6]], 5, 4, 9),
        ([[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], 5, 4, 14),
        ([[0,3],[6,4],[8,5]], 3, 2, 0),
        ([[200000,10000]], 200000, 0, 10000),
        ([[200000,10000]], 0, 200000, 10000),
        ([[0,7],[7,4],[10,9],[11,4],[13,2],[14,8]], 3, 2, 0),
        ([[0,10000]], 100000, 100000, 0)
    ]

    for i, (fruits, startPos, k, expected) in enumerate(test_cases):
        result = sol.maxTotalFruits(fruits, startPos, k)
        print(f"Test case {i + 1}: Fruits = {fruits}, Start = {startPos}, K = {k} → Result = {result} (Expected: {expected}) {'✅' if result == expected else '❌'}")

if __name__ == "__main__":
    main()