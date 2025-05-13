class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        for _ in range(t):
            new_freq = [0] * 26
            new_freq[0] += freq[25]
            new_freq[1] += freq[25]
            for i in range(25):
                new_freq[i+1] = (new_freq[i+1] + freq[i]) % MOD
            for i in range(26):
                new_freq[i] %= MOD
            freq = new_freq
        return sum(freq) % MOD
if __name__ == '__main__':
    #Input: s = "abcyy", t = 2
    #Output: 7
    #Input: s = "azbk", t = 1
    #Output: 5
    #extr
    #Test Case:
    #s = "jqktcurgdvlibczdsvnsg"
    #t = 7517
    #Expected Output:
    #79033769
    
    s = input().strip()
    t = int(input().strip()) 
    sol = Solution()
    resultado = sol.lengthAfterTransformations(s, t)
    print(resultado)
