class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        """
        Devuelve True si existe una permutación de los dígitos de n (sin ceros
        a la izquierda) que sea una potencia de 2.
        """
        # cadena con los dígitos de n ordenados (representa el multiconjunto de dígitos)
        digitos_ordenados = ''.join(sorted(str(n)))

        # precomputar conjunto de representaciones ordenadas de 2^0 .. 2^30
        conjunto_potencias = { ''.join(sorted(str(1 << exponente))) for exponente in range(31) }

        # si la representación ordenada de n aparece en el conjunto, existe la permutación buscada
        return digitos_ordenados in conjunto_potencias


# Bloque de pruebas básicas
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        (1, True),
        (10, False),
        (16, True),     # 16 es potencia de 2
        (46, True),     # puede reordenarse a 64
        (821, True),    # puede reordenarse a 128
        (218, True),    # otra permutación de 128
        (1000000000, False)
    ]
    for entrada, esperado in test_cases:
        resultado = sol.reorderedPowerOf2(entrada)
        print(f"{entrada} -> {resultado} (esperado: {esperado})")
