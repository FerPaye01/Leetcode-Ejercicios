class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 0:
            return []
        
        triangulo = [[1]]
        
        for i in range(1, numRows):
            fila_anterior = triangulo[i-1]
            nueva_fila = [1]
            
            for j in range(1, i):
                nueva_fila.append(fila_anterior[j-1] + fila_anterior[j])
            
            nueva_fila.append(1)
            triangulo.append(nueva_fila)
        
        return triangulo

def main():
    sol = Solution()
    
    test_cases = [
        (1, [[1]]),
        (2, [[1], [1,1]]),
        (3, [[1], [1,1], [1,2,1]]),
        (4, [[1], [1,1], [1,2,1], [1,3,3,1]]),
        (5, [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]),
        (6, [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1], [1,5,10,10,5,1]])
    ]
    
    for i, (numRows, expected) in enumerate(test_cases):
        result = sol.generate(numRows)
        print(f"Test case {i+1}: numRows = {numRows}")
        print(f"  Resultado: {result}")
        print(f"  Esperado: {expected}")
        print(f"  {'✅' if result == expected else '❌'}")
        print()

if __name__ == "__main__":
    main()