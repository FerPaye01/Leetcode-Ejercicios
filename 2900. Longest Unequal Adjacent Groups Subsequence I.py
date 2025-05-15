class Solution:
    def getLongestSubsequence(self, words, groups):
        result = [words[0]]# siempre se incluye la primera palabra en el resultado
        last_group = groups[0]  # se guarda el último grupo visto
        # se agregan palabras de manera codiciosa cada vez que el grupo cambia
        for i in range(1, len(groups)):
            if groups[i] != last_group:  # conparacion de si el grupo actual es diferente al anterior
                result.append(words[i])  # append de la palabra al resultado
                last_group = groups[i]  # actualizamos el grupo anterior
        
        return result  # se devuekve la subsecuencia más larga con alternancia de grupo


if __name__ == "__main__":

    words1 = ["e", "a", "b"]
    groups1 = [0, 0, 1]
    sol = Solution()
    print(sol.getLongestSubsequence(words1, groups1))  # esperado: ['e', 'b']
    
    words2 = ["a", "b", "c", "d"]
    groups2 = [1, 0, 1, 1]
    print(sol.getLongestSubsequence(words2, groups2))  #  esperado: ['a', 'b', 'c']
