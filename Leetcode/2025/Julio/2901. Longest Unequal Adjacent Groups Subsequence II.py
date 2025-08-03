class Solution:
    def getWordsInLongestSubsequence(self, words, groups):
        n = len(words)
        dp = [1] * n   # dp[i] representa la longitud de la mejor subsecuencia que termina en la palabra i
        prev = [-1] * n  # prev[i] guarda el índice anterior en la subsecuencia óptima que termina en i

        # construir DP iterando sobre cada par de palabras (j, i) con j < i
        for i in range(n):
            for j in range(i):
                # condiciones: las palabras deben pertenecer a grupos distintos y tener misma longitud
                if groups[i] != groups[j] and len(words[i]) == len(words[j]):
                    # se calcula la distancia Hamming (diferencias entre caracteres)
                    diff = 0
                    for c1, c2 in zip(words[i], words[j]):
                        if c1 != c2:
                            diff += 1
                            if diff > 1:  # si hay más de una diferencia, no se cumple la condición
                                break
                    # si hay exactamente una diferencia y se mejora la subsecuencia
                    if diff == 1 and dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j 

        # se debe de encontrar el fin de la subsecuencia más larga (el índice donde termina la subsecuencia más larga)
        max_len = 0
        idx = 0
        for i in range(n):
            if dp[i] > max_len:
                max_len = dp[i]
                idx = i

        # se reconstruye la subsecuencia óptima desde el último elemento hacia el primero
        subseq = []
        while idx != -1:
            subseq.append(words[idx])
            idx = prev[idx]
        
        return subseq[::-1] # como se construyó hacia atrás, se invierte para devolverla en orden correcto


if __name__ == "__main__":
    words1 = ["bab", "dab", "cab"]
    groups1 = [1, 2, 2]
    result1 = Solution().getWordsInLongestSubsequence(words1, groups1)
    print("Ejemplo 1:", result1)  # esperado : ["bab","cab"] o ["bab","dab"]
    words2 = ["a", "b", "c", "d"]
    groups2 = [1, 2, 3, 4]
    result2 = Solution().getWordsInLongestSubsequence(words2, groups2)
    print("Ejemplo 2:", result2)  # ["a","b","c","d"]
