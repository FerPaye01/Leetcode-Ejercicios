class Solution(object):
    def maxDifference(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        best = float('-inf')
        chars = [str(i) for i in range(5)]
        class SegmentTree:
            def __init__(self, size):
                self.N = 1
                while self.N < size:
                    self.N <<= 1
                self.tree = [10**18] * (2 * self.N)
            def update(self, idx, val):
                i = idx + self.N
                if val < self.tree[i]:
                    self.tree[i] = val
                    i //= 2
                    while i:
                        self.tree[i] = min(self.tree[2*i], self.tree[2*i+1])
                        i //= 2
            
            def query(self, l, r):
                res = 10**18
                l += self.N; r += self.N
                while l <= r:
                    if l & 1:
                        res = min(res, self.tree[l]); l += 1
                    if not (r & 1):
                        res = min(res, self.tree[r]); r -= 1
                    l //= 2; r //= 2
                return res
        
        for a in chars:
            for b in chars:
                if a == b:
                    continue
                countA = [0]*(n+1)
                countB = [0]*(n+1)
                pa = [0]*(n+1)
                pb = [0]*(n+1)
                score = [0]*(n+1)
                for i in range(1, n+1):
                    countA[i] = countA[i-1] + (s[i-1]==a)
                    countB[i] = countB[i-1] + (s[i-1]==b)
                    pa[i] = countA[i] & 1
                    pb[i] = countB[i] & 1
                    score[i] = countA[i] - countB[i]
                totalB = countB[n]
                size = totalB + 1
                inf = 10**18
                trees = { (x,y): SegmentTree(size) for x in (0,1) for y in (0,1) }
                trees[(pa[0], pb[0])].update(countB[0], score[0])
                res_ab = float('-inf')
                for j in range(k, n+1):
                    i = j - k
                    trees[(pa[i], pb[i])].update(countB[i], score[i])
                    need = (pa[j]^1, pb[j])
                    thr = countB[j] - 2
                    if thr >= 0:
                        best_pref = trees[need].query(0, thr)
                        if best_pref < inf:
                            res_ab = max(res_ab, score[j] - best_pref)
                
                if res_ab != float('-inf'):
                    best = max(best, res_ab)
        return best if best != float('-inf') else -1
if __name__ == '__main__':
    test_cases = [
        ("12233", 4),
        ("1122211", 3),
        ("110", 3), 
    ]
    sol = Solution()
    for s, k in test_cases:
        result = sol.maxDifference(s, k)
        print(result)
"""Example 1:
Input: s = "12233", k = 4

Output: -1

Explanation:

For the substring "12233", the frequency of '1' is 1 and the frequency of '3' is 2. The difference is 1 - 2 = -1.

Example 2:

Input: s = "1122211", k = 3

Output: 1

Explanation:

For the substring "11222", the frequency of '2' is 3 and the frequency of '1' is 2. The difference is 3 - 2 = 1.

Example 3:

Input: s = "110", k = 3

Output: -1

 """