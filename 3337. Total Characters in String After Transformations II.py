class Solution:
 
    def lengthAfterTransformations(self, s, t, nums):
        MOD = 10**9 + 7
        # Construir la matriz de transición M (26×26)
        M = [[0]*26 for _ in range(26)]
        for i in range(26):
            k = nums[i]
            for step in range(1, k+1):
                j = (i + step) % 26
                M[j][i] += 1

        # Multiplicación de matrices 26×26
        def mat_mult(A, B):
            C = [[0]*26 for _ in range(26)]
            for i in range(26):
                for k in range(26):
                    if A[i][k]:
                        aik = A[i][k]
                        for j in range(26):
                            C[i][j] = (C[i][j] + aik * B[k][j]) % MOD
            return C

        # Exponenciación rápida de matriz
        def mat_pow(mat, exp):
            # Identidad
            res = [[1 if i == j else 0 for j in range(26)] for i in range(26)]
            base = mat
            while exp > 0:
                if exp & 1:
                    res = mat_mult(res, base)
                base = mat_mult(base, base)
                exp >>= 1
            return res

        # Calculamos M^t
        Mt = mat_pow(M, t)

        # Vector inicial de frecuencias
        v0 = [0]*26
        for ch in s:
            v0[ord(ch) - 97] += 1

        total = 0
        for i in range(26):
            row = Mt[i]
            for j in range(26):
                if row[j] and v0[j]:
                    total = (total + row[j] * v0[j]) % MOD

        return total


if __name__ == '__main__':
    
    s = input().strip()
    t = int(input().strip())
    nums = list(map(int, input().split()))
    result = Solution().lengthAfterTransformations(s, t, nums)
    print(result)
