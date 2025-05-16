class Solution:
    def getWordsInLongestSubsequence(self, words, groups):
        n = len(words)
        dp = [1] * n
        prev = [-1] * n

        # construir DP
        for i in range(n):
            for j in range(i):
                if groups[i] != groups[j] and len(words[i]) == len(words[j]):
                    diff = 0
                    for c1, c2 in zip(words[i], words[j]):
                        if c1 != c2:
                            diff += 1
                            if diff > 1:
                                break
                    if diff == 1 and dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j

        max_len = 0
        idx = 0
        for i in range(n):
            if dp[i] > max_len:
                max_len = dp[i]
                idx = i

        subseq = []
        while idx != -1:
            subseq.append(words[idx])
            idx = prev[idx]

        return subseq[::-1]


if __name__ == "__main__":
    words1 = ["bab", "dab", "cab"]
    groups1 = [1, 2, 2]
    result1 = Solution().getWordsInLongestSubsequence(words1, groups1)
    print("Ejemplo 1:", result1)  # esperado : ["bab","cab"] o ["bab","dab"]

    # Ejempl 2
    words2 = ["a", "b", "c", "d"]
    groups2 = [1, 2, 3, 4]
    result2 = Solution().getWordsInLongestSubsequence(words2, groups2)
    print("Ejemplo 2:", result2)  # esperado : ["a","b","c","d"]
