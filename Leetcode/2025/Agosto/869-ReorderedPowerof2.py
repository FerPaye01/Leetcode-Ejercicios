class Solution: 
     # Clase contenedora que expone la interfaz 'reorderedPowerOf2' utilizada en plataformas como LeetCode.
    def reorderedPowerOf2(self, n: int) -> bool:  
        # Método público: recibe un entero n y retorna True si alguna permutación válida de sus dígitos es potencia de 2.
        digitos_ordenados = ''.join(sorted(str(n)))  
        # Representación canónica del multiconjunto de dígitos: convertir a cadena, ordenar y concatenar (coste O(d log d)).
        conjunto_potencias = {''.join(sorted(str(1 << exponente))) for exponente in range(31)} 
        # Precomputación de multiconjuntos de dígitos para 2^0..2^30 (2^30 > 10**9), almacenamiento en conjunto para búsqueda O(1) amortizada.
        return digitos_ordenados in conjunto_potencias  
    # Comprobación de pertenencia en el conjunto precomputado; devuelve booleano según coincidencia exacta del multiconjunto.

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
