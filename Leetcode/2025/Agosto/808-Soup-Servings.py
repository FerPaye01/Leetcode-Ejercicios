from functools import lru_cache
import math

class Solution:
    def soupServings(self, n: int) -> float:
        # Caso trivial
        if n == 0:
            return 0.5
        
        # Para n grandes la probabilidad converge a 1.0 (umbral seguro para precisión 1e-5).
        if n >= 4800:
            return 1.0
        
        # Escalamos a unidades de 25 mL
        unidades = math.ceil(n / 25)
        
        @lru_cache(None)
        def prob(a: int, b: int) -> float:
            # Casos base según enunciado
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
            
            # Transiciones: (100,0), (75,25), (50,50), (25,75)
            return 0.25 * (
                prob(a - 4, b) +
                prob(a - 3, b - 1) +
                prob(a - 2, b - 2) +
                prob(a - 1, b - 3)
            )
        
        return prob(unidades, unidades)


def main():
    sol = Solution()
    
    # (n, esperado) → esperado tomado del enunciado o calculado manualmente
    test_cases = [
        (50, 0.62500),         # ejemplo 1
        (100, 0.71875),        # ejemplo 2
        (0, 0.5),              # ambos empiezan vacíos → empate
        (25, 0.625),           # escala pequeña
        (4800, 1.0),           # umbral de aproximación
        (10000, 1.0)           # n muy grande
    ]
    
    for i, (n, esperado) in enumerate(test_cases, start=1):
        resultado = sol.soupServings(n)
        print(f"Test case {i}: n = {n}")
        print(f"  Resultado: {resultado:.5f}")
        print(f"  Esperado: {esperado:.5f}")
        print(f"  {'✅' if abs(resultado - esperado) < 1e-5 else '❌'}")
        print()

if __name__ == "__main__":
    main()
